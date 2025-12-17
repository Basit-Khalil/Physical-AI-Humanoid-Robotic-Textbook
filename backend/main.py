from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import logging
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
import os

# LLM integration
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Database imports for Neon/PostgreSQL
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import urllib.parse

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Qdrant client - using local instance for now, can be changed to cloud
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333")  # Default to local instance
)

# Create a collection for document chunks if it doesn't exist
collection_name = "document_chunks"
try:
    qdrant_client.get_collection(collection_name)
except:
    # Create collection with appropriate vector size (384 for all-MiniLM-L6-v2)
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
    print(f"Created collection: {collection_name}")

# Database setup for Neon/PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/dbname")

# Properly encode the URL to handle special characters
encoded_url = urllib.parse.quote_plus(DATABASE_URL)
engine = create_engine(f"postgresql+asyncpg://{encoded_url}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    session_title = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer)
    user_id = Column(Integer)
    message_content = Column(Text)
    is_user_message = Column(Boolean, default=True)  # True for user, False for bot
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for chat request
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Native Book Backend!"}

# Simple chat endpoint
@app.post("/chat")
def chat(chat_request: ChatRequest):
    # Placeholder response - in the future, this will connect to RAG, LLM, etc.
    user_message = chat_request.message
    # Simulate processing
    bot_response = f"Echo: {user_message} (This will be replaced by RAG/LLM response)"

    # Store the chat message in the database
    # Note: In a real implementation, you'd get the user_id from authentication
    # For now, we'll use a placeholder user_id
    from sqlalchemy.orm import Session
    db = SessionLocal()

    try:
        # Create a new chat message record
        chat_message_user = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=user_message,
            is_user_message=True
        )
        db.add(chat_message_user)

        # Create a record for the bot's response
        chat_message_bot = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=bot_response,
            is_user_message=False
        )
        db.add(chat_message_bot)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error storing chat message: {e}")
    finally:
        db.close()

    return {"response": bot_response}

# Endpoint to add a document and generate embeddings
@app.post("/add_document")
def add_document(text: str):
    """
    Adds a document to the system, chunks it, and generates embeddings.
    Stores the chunks and embeddings in Qdrant vector database.
    """
    # Simple chunking: split by paragraphs
    chunks = text.split('\n\n')
    # Filter out empty chunks and chunks with less than 10 characters
    chunks = [chunk.strip() for chunk in chunks if len(chunk.strip()) > 10]

    # Generate embeddings for each chunk
    embeddings = model.encode(chunks)

    # Prepare points for Qdrant
    from time import time
    points = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        # Use timestamp-based ID to ensure uniqueness
        point_id = int(time() * 1000000) + i  # microseconds timestamp + index
        point = PointStruct(
            id=point_id,  # Use integer ID
            vector=embedding.tolist(),  # Convert numpy array to list
            payload={"text": chunk, "chunk_id": i}
        )
        points.append(point)

    # Upload points to Qdrant
    qdrant_client.upsert(
        collection_name=collection_name,
        points=points
    )

    return {"message": f"Added {len(chunks)} chunks to the Qdrant vector store."}

# Function to find the most similar chunk to a query using Qdrant
def find_most_similar_chunk(query_embedding, top_k=3):
    """
    Finds the most similar chunk to the query using Qdrant similarity search.
    """
    # Perform similarity search in Qdrant
    search_results = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_embedding.tolist(),
        limit=top_k
    )

    # Extract the text from the search results
    similar_chunks = []
    for result in search_results:
        similar_chunks.append(result.payload["text"])

    return similar_chunks

# Function to generate response using retrieved context and LLM
def generate_response_with_context(user_query: str, retrieved_chunks: list):
    """
    Generates a response using the user query and retrieved context chunks.
    """
    if not retrieved_chunks:
        return "I couldn't find any relevant information to answer your question."

    # Combine the retrieved chunks into a context string
    context = "\n\n".join(retrieved_chunks)

    # Create a prompt for the LLM with the context and user query
    prompt = f"""
    You are an AI assistant for the AI-Native Software Development Book.
    Use the following context to answer the user's question.
    If the context doesn't contain the information needed, say so.

    Context:
    {context}

    User Question: {user_query}

    Answer:
    """

    try:
        # Use OpenAI API to generate a response
        client = OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can change this to gpt-4 if preferred
            messages=[
                {"role": "system", "content": "You are a helpful assistant for the AI-Native Software Development Book. Answer questions based on the provided context."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response with LLM: {e}")
        # Fallback response if LLM fails
        return f"I found some relevant information: {' '.join(retrieved_chunks[:2])}. Please check the book for more details."

# Endpoint to search for relevant chunks based on a query
@app.post("/search")
def search(query: str):
    """
    Searches for relevant chunks based on a query using Qdrant vector database.
    """
    # Generate embedding for the query
    query_embedding = model.encode([query])[0]

    # Find the most similar chunks using Qdrant
    most_similar_chunks = find_most_similar_chunk(query_embedding, top_k=3)

    return {"chunks": most_similar_chunks}

# Enhanced chat endpoint with RAG (Retrieval Augmented Generation)
@app.post("/chat_with_rag")
def chat_with_rag(chat_request: ChatRequest):
    """
    Chat endpoint that uses RAG (Retrieval Augmented Generation) to provide context-aware responses.
    """
    user_message = chat_request.message

    # Generate embedding for the user query
    query_embedding = model.encode([user_message])[0]

    # Find the most similar chunks using Qdrant
    retrieved_chunks = find_most_similar_chunk(query_embedding, top_k=3)

    # Generate a response using the retrieved context and LLM
    bot_response = generate_response_with_context(user_message, retrieved_chunks)

    # Store the chat message in the database
    # Note: In a real implementation, you'd get the user_id from authentication
    from sqlalchemy.orm import Session
    db = SessionLocal()

    try:
        # Create a new chat message record
        chat_message_user = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=user_message,
            is_user_message=True
        )
        db.add(chat_message_user)

        # Create a record for the bot's response
        chat_message_bot = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=bot_response,
            is_user_message=False
        )
        db.add(chat_message_bot)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error storing chat message: {e}")
    finally:
        db.close()

    return {"response": bot_response}

# Pydantic model for selected text chat request
class SelectedTextChatRequest(BaseModel):
    message: str
    selected_text: str

# Endpoint for answering questions based only on selected text
@app.post("/chat_selected_text")
def chat_selected_text(chat_request: SelectedTextChatRequest):
    """
    Chat endpoint that answers questions based only on the provided selected text.
    This allows users to ask questions about specific text they've selected.
    """
    user_message = chat_request.message
    selected_text = chat_request.selected_text

    # Create a prompt that specifically uses only the selected text as context
    prompt = f"""
    You are an AI assistant for the AI-Native Software Development Book.
    Answer the user's question using ONLY the provided selected text as context.
    Do not use any other knowledge or information beyond what's in the selected text.
    If the selected text doesn't contain the information needed to answer the question, say so.

    Selected Text:
    {selected_text}

    User Question: {user_message}

    Answer:
    """

    try:
        # Use OpenAI API to generate a response based only on the selected text
        client = OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can change this to gpt-4 if preferred
            messages=[
                {"role": "system", "content": "You are a helpful assistant for the AI-Native Software Development Book. Answer questions based only on the provided selected text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )

        bot_response = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response with LLM: {e}")
        # Fallback response if LLM fails
        bot_response = f"I found the selected text: {selected_text[:200]}... Please check this section for more details."

    # Store the chat message in the database
    # Note: In a real implementation, you'd get the user_id from authentication
    from sqlalchemy.orm import Session
    db = SessionLocal()

    try:
        # Create a new chat message record
        chat_message_user = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=f"Question about selected text: {user_message}",
            is_user_message=True
        )
        db.add(chat_message_user)

        # Create a record for the bot's response
        chat_message_bot = ChatMessage(
            session_id=1,  # Placeholder session ID
            user_id=1,     # Placeholder user ID
            message_content=bot_response,
            is_user_message=False
        )
        db.add(chat_message_bot)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error storing chat message: {e}")
    finally:
        db.close()

    return {"response": bot_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # Using port 8001 to avoid conflict with Docusaurus dev server