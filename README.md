# Groq AI Productivity Assistant API

## Overview

This project converts the Day 5 Groq AI Productivity Assistant CLI application into a FastAPI-based REST API. Users can send tasks through API requests and receive AI-generated responses powered by Groq.

## Features

* FastAPI integration
* POST /generate endpoint
* Bearer Token authentication
* Response saved to outputs/response.txt
* Environment variables using .env
* Health check endpoint
* Optional output retrieval endpoint

## Project Structure

```text
grok_qna_api/
│
├── api.py
├── .env
├── .env.example
├── requirements.txt
├── README.md
│
└── outputs/
    └── response.txt
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
API_SECRET_TOKEN=mytoken123
```

## Run the Application

```bash
python -m uvicorn api:app --reload
```

Open Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /

Health check endpoint.

### POST /generate

Generate an AI response from a task.

Header:

```text
Authorization: Bearer mytoken123
```

Request Body:

```json
{
  "task": "Create a 3-day FastAPI study plan"
}
```

### GET /outputs

Returns the latest saved output from `outputs/response.txt`.

## Status Codes

* 200 OK
* 400 Bad Request
* 401 Unauthorized
* 500 Internal Server Error

## Technologies Used

* Python
* FastAPI
* Groq API
* Uvicorn
* Pydantic
* Python-Dotenv
