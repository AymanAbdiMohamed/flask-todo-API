# Flask Todo API

A simple Flask API for managing todos with in-memory storage.

## Overview

This is a RESTful Todo API built with Flask that allows you to create, read, update, and delete todos. Each todo is stored in memory as a dictionary with the following structure:

```json
{
  "id": 1,
  "title": "Learn Flask",
  "completed": false
}
```

## Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install flask
```

### Running the Application

```bash
python main.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Get All Todos
- **Endpoint:** `GET /todos`
- **Response:** List of all todos

### Get a Single Todo
- **Endpoint:** `GET /todos/<id>`
- **Response:** A specific todo by ID

### Create a New Todo
- **Endpoint:** `POST /todos`
- **Request Body:**
```json
{
  "title": "Todo title",
  "completed": false
}
```
- **Response:** Created todo with ID

### Update a Todo
- **Endpoint:** `PUT /todos/<id>`
- **Request Body:**
```json
{
  "title": "Updated title",
  "completed": true
}
```
- **Response:** Updated todo

### Delete a Todo
- **Endpoint:** `DELETE /todos/<id>`
- **Response:** Confirmation message
