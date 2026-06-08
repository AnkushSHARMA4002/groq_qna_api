from fastapi import FastAPI
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()

key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=key)

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/ask")
def ask(question: str):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }