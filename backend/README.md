# AI-Native Book Backend

This directory contains the FastAPI backend for the AI-Native Software Development Book project. It handles the RAG chatbot, personalization, and translation features.

## Setup

1.  Ensure you have Python 3.7+ installed.
2.  Navigate to this directory (`backend`).
3.  It's recommended to create a virtual environment:
    `python -m venv venv`
    `source venv/bin/activate` (On Windows: `venv\Scripts\activate`)
4.  Install the required dependencies:
    `pip install -r requirements.txt`
5.  Run the development server:
    `python main.py`
    The server will start, typically at `http://0.0.0.0:8001`.

## Endpoints

Currently, the backend only has a root endpoint (`/`) which returns a welcome message. More endpoints will be added for RAG, personalization, and translation.