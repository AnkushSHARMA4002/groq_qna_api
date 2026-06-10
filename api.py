from fastapi import FastAPI, Header, HTTPException
from groq import Groq
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=key)

SECRET_TOKEN = "mytoken123"

outputs = []


class TaskRequest(BaseModel):
    task: str


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


@app.post("/generate")
def generate(
    data: TaskRequest,
    authorization: str = Header(None)
):

    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization token missing"
        )

    if authorization != SECRET_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    if data.task.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Task cannot be empty"
        )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": data.task}
        ]
    )

    result = response.choices[0].message.content

    outputs.append(result)

    return {
        "output": result
    }


@app.get("/outputs")
def get_outputs():
    return {
        "outputs": outputs
    }

@app.get("/test-header")
def test_header(authorization: str = Header(None)):
    return {
        "authorization": authorization
    }