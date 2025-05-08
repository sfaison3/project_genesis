# Genesis Music Learning App

Repository for ASU AI Spark Challenge

Genesis is a music learning app that helps users generate custom songs about topics they're studying. It leverages AI models to create educational content that makes learning more fun and engaging through rhythm, rhyme, and repetition.

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
- `GET /api/music/genres` - List available music genres
- `POST /api/generate` - Generate learning content based on input

## Features

- Model Context Protocol (MCP) that routes requests to the appropriate AI model
- Custom song generation using Beatoven.ai API for creating music in various genres
- Support for text, image, and video generation alongside music
- Interactive UI for creating educational content that makes learning engaging
- Ability to specify learning topics, preferred genres, and song duration

## Deployment to Render

The project is set up for easy deployment on Render using Docker:

1. **Fork/Push** this repository to your GitHub account
2. **Connect your GitHub account** to Render
3. **Create a new Web Service** on Render
   - Select "Deploy from GitHub repo"
   - Choose this repository
   - Select "Use render.yaml" for configuration
4. **Set Environment Variables** in the Render dashboard:
   - Add your `OPENAI_API_KEY`
   - Add your `GOOGLE_API_KEY`
5. **Deploy** the service

Alternatively, you can deploy manually:

1. **Connect GitHub repo** to Render
2. Create a **Web Service** with the following settings:
   - Environment: Docker
   - Region: Choose the one closest to your users
   - Branch: main
   - Plan: Free (or choose a paid plan for better performance)
   - Health Check Path: `/api/health`
   - Environment Variables:
     - `PORT`: 10000
     - `API_HOST`: 0.0.0.0
     - `API_PORT`: 10000
     - `OPENAI_API_KEY`: Your OpenAI API Key
     - `GOOGLE_API_KEY`: Your Google API Key
     - `BEATOVEN_API_KEY`: Your Beatoven.ai API Key