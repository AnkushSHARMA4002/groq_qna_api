# Groq AI Productivity Assistant

## Overview

Groq AI Productivity Assistant is a Python application powered by the Groq API. It helps users generate AI-based responses for productivity-related tasks such as study plans, learning roadmaps, summaries, task breakdowns, and other planning activities.

This project was later extended with a FastAPI wrapper to expose the functionality through REST APIs.

## Features

* AI-powered task assistance using Groq
* Fast and efficient response generation
* FastAPI integration
* REST API endpoints
* Bearer Token authentication
* Environment variable configuration using `.env`
* Response storage in `outputs/response.txt`
* Swagger documentation support

## Technologies Used

* Python
* FastAPI
* Groq API
* Uvicorn
* Pydantic
* Python Dotenv
* Git & GitHub

## Project Structure

grok_qna_api/

├── api.py

├── .env

├── .env.example

├── .gitignore

├── requirements.txt

├── README.md

├── outputs/

│ └── response.txt

└── screenshots/

## Installation

Clone the repository:

```bash
git clone https://github.com/AnkushSHARMA4002/groq_qna_api.git
```

Navigate to the project folder:

```bash
cd groq_qna_api
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

```

## Running the Application

Start the FastAPI server:

```bash
python -m uvicorn api:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /

Returns API health status.

### POST /generate

Generates an AI response for a given task.

### GET /outputs

Returns the latest saved output.

## Status Codes

* 200 OK
* 400 Bad Request
* 401 Unauthorized
* 500 Internal Server Error

## Author

Ankush Sharma
