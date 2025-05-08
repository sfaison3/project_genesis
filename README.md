# Genesis - Multi-modal AI Orchestration Platform

Repository for 1st ASU AI Spark Challenge

Genesis is an AI orchestration platform that seamlessly switches between multiple AI models for image, video, and text generation.

## Project Structure

- `app/` - FastAPI backend
- `frontend/` - Vue.js frontend

## Getting Started

### Environment Setup

Create `.env` files in both the root directory, app directory, and frontend directory using the provided `.env.example` files as templates.

### Backend Setup

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

The FastAPI backend will be available at http://localhost:8000 with interactive docs at http://localhost:8000/docs

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The Vue.js frontend will be available at http://localhost:5173

The frontend will proxy API requests to the backend, so both can run simultaneously on different ports.

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/models` - List available AI models
- `POST /api/generate` - Generate content based on input

## Features

- Model Context Protocol (MCP) that routes requests to the appropriate AI model
- Support for text, image, and video generation
- Interactive UI for submitting prompts and viewing results