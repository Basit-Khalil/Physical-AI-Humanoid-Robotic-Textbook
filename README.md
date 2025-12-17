# AI-Native Software Development Book + Docusaurus Website + Integrated RAG Chatbot

This project implements a comprehensive AI-Native Software Development educational platform featuring a Docusaurus-based book website with an integrated RAG (Retrieval-Augmented Generation) chatbot.

## Features

### Frontend (Docusaurus)
- Complete book structure with 4 modules and weekly breakdowns
- Module 1: Foundations of AI-Native Software Development
- Module 2: Retrieval-Augmented Generation (RAG) Systems
- Module 3: User Experience and Personalization
- Module 4: Reusable Intelligence and Deployment
- Responsive design with React components
- Integrated chatbot interface

### Backend (FastAPI)
- RAG pipeline with text chunking and embedding generation
- Qdrant vector database integration for efficient similarity search
- Neon Serverless Postgres for user data and metadata storage
- OpenAI integration for intelligent responses
- Multiple chat endpoints:
  - Basic chat functionality
  - RAG-powered contextual responses
  - Selected text-only answering mode

### Core Capabilities
- Text embedding using Sentence Transformers
- Vector similarity search with cosine similarity
- Context-aware question answering
- Selected text processing for focused responses
- Urdu translation placeholders
- User personalization features

## Architecture

### Tech Stack
- **Frontend**: Docusaurus, React
- **Backend**: FastAPI, Python
- **Vector Database**: Qdrant
- **Relational Database**: PostgreSQL (Neon Serverless)
- **AI/ML**: Sentence Transformers, OpenAI GPT
- **Containerization**: Docker Compose

### Data Flow
1. Documents are chunked and embedded using Sentence Transformers
2. Embeddings are stored in Qdrant vector database
3. User queries are embedded and matched against stored vectors
4. Relevant chunks are retrieved and used to generate contextual responses
5. User interactions are stored in PostgreSQL for analytics and personalization

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker and Docker Compose
- OpenAI API key

### Installation

1. Clone the repository
2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```bash
   cd book
   npm install
   ```

4. Set up environment variables:
   ```bash
   # Copy the .env file and add your OpenAI API key
   cp .env .env.local
   # Edit .env.local to add your API key
   ```

5. Start Qdrant vector database:
   ```bash
   docker-compose up -d
   ```

6. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```

7. Start the Docusaurus frontend:
   ```bash
   cd book
   npm start
   ```

### Environment Variables

Create a `.env.local` file with the following variables:

```
# Qdrant Configuration
QDRANT_URL=http://localhost:6333

# Database Configuration (Update with your Neon credentials)
DATABASE_URL=postgresql://username:password@localhost/dbname

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
```

## API Endpoints

### Backend API (running on port 8001)
- `GET /` - Health check
- `POST /chat` - Basic chat endpoint
- `POST /chat_with_rag` - RAG-powered chat with contextual responses
- `POST /chat_selected_text` - Chat focused on selected text only
- `POST /add_document` - Add documents to the vector store
- `POST /search` - Search for relevant chunks

### Frontend (running on port 3001)
- `/` - Book homepage
- `/chat` - Chatbot interface

## Usage

1. **Adding Content**: Use the `/add_document` endpoint to add book content to the vector store
2. **Chatting**: Use the chat interface to ask questions about the book content
3. **Contextual Responses**: The RAG system will retrieve relevant information and generate contextual answers
4. **Selected Text Mode**: Select text in the book and ask questions specifically about that content

## Development

The project follows an AI-Native development approach with Claude Code integration for automated development tasks. All components are designed to work together seamlessly while maintaining modularity for future enhancements.

## Deployment

The system is designed for deployment to GitHub Pages (frontend) and a cloud provider (backend) with Neon Postgres and Qdrant cloud instances.
