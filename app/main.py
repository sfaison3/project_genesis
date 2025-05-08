from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Literal, List
import uvicorn
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Genesis Music Learning API", description="Generate custom songs to enhance learning")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
BEATOVEN_API_KEY = os.getenv("BEATOVEN_API_KEY")

# Check if API keys are available
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not found in environment variables")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not found in environment variables")
if not BEATOVEN_API_KEY:
    print("Warning: BEATOVEN_API_KEY not found in environment variables")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class GenerateRequest(BaseModel):
    input: str
    model: Optional[str] = "auto"  # auto, gpt-image-1, veo2, gemini, o4-mini, beatoven
    genre: Optional[str] = "pop"  # For music generation - pop, rock, jazz, classical, etc.
    duration: Optional[int] = 60  # Duration in seconds for music generation
    learning_topic: Optional[str] = None  # Topic the user is learning about

class GenerateResponse(BaseModel):
    output: str
    type: Literal["text", "image", "video", "music"]
    model_used: str

class MusicGenreOption(BaseModel):
    id: str
    name: str
    description: str

# Model Context Protocol (MCP) - Simple implementation
def determine_best_model(input_text: str, requested_model: str) -> str:
    """Determine the best model based on input and request"""
    if requested_model != "auto":
        return requested_model
        
    # Very simple heuristic, would be more sophisticated in production
    if "picture" in input_text.lower() or "image" in input_text.lower():
        return "gpt-image-1"
    elif "video" in input_text.lower() or "animation" in input_text.lower():
        return "veo2"
    elif "song" in input_text.lower() or "music" in input_text.lower() or "melody" in input_text.lower():
        return "beatoven"
    elif len(input_text) > 100:  # Longer requests might be better for o4-mini
        return "o4-mini"
    else:
        return "gemini"  # Default

# Beatoven.ai API Helpers
def get_beatoven_genres():
    """Get available genres from Beatoven.ai API"""
    # In a real implementation, we would fetch from Beatoven API
    # For now, return hardcoded options
    return [
        {"id": "pop", "name": "Pop", "description": "Popular music with catchy melodies"},
        {"id": "rock", "name": "Rock", "description": "Guitar-driven energetic music"},
        {"id": "jazz", "name": "Jazz", "description": "Improvisational complex harmonies"},
        {"id": "classical", "name": "Classical", "description": "Traditional orchestral music"},
        {"id": "electronic", "name": "Electronic", "description": "Digital synthesized music"},
        {"id": "hip_hop", "name": "Hip Hop", "description": "Rhythmic beats with spoken lyrics"},
        {"id": "country", "name": "Country", "description": "Folk-influenced American music"},
        {"id": "folk", "name": "Folk", "description": "Traditional acoustic cultural music"}
    ]

def generate_music(genre: str, duration: int, topic: str):
    """Generate music using Beatoven.ai API"""
    # In a production implementation, we would call the actual Beatoven API:
    # https://github.com/Beatoven/public-api/blob/main/docs/api-spec.md
    
    if not BEATOVEN_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Beatoven API key is required but not configured"
        )
        
    # Mock implementation - would be replaced with actual API call
    # Example: POST to https://api.beatoven.ai/v1/tracks with appropriate params
    
    # Example of what the code would look like with real API integration:
    """
    try:
        response = requests.post(
            "https://api.beatoven.ai/v1/tracks",
            headers={"Authorization": f"Bearer {BEATOVEN_API_KEY}"},
            json={
                "name": f"Learning about {topic}",
                "duration": duration,
                "genre": genre,
                "mood": "inspirational"
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["preview_url"]  # or however the API returns the music URL
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Beatoven API error: {str(e)}")
    """
    
    # For prototype, return a placeholder MP3 URL
    return f"https://placehold.co/400x100.mp3?text=AI+Music+{genre}+about+{topic}"

# Routes
@app.get("/api/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "ok"}

@app.get("/api/models")
async def list_models():
    """List available AI models"""
    return {
        "models": [
            {"id": "gpt-image-1", "provider": "OpenAI", "type": "image"},
            {"id": "veo2", "provider": "Google", "type": "video"},
            {"id": "gemini", "provider": "Google", "type": "text"},
            {"id": "o4-mini", "provider": "OpenAI", "type": "text"},
            {"id": "beatoven", "provider": "Beatoven.ai", "type": "music"}
        ]
    }

@app.get("/api/music/genres", response_model=List[MusicGenreOption])
async def list_music_genres():
    """List available music genres"""
    return get_beatoven_genres()

@app.post("/api/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """Generate content based on input using MCP routing"""
    try:
        # Determine which model to use via MCP
        model = determine_best_model(request.input, request.model)
        
        # Check if required API keys are available
        if model in ["gpt-image-1", "o4-mini"] and not OPENAI_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="OpenAI API key is required but not configured"
            )
        if model in ["veo2", "gemini"] and not GOOGLE_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="Google API key is required but not configured"
            )
        if model == "beatoven" and not BEATOVEN_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="Beatoven API key is required but not configured"
            )
        
        # This would call the actual AI services in production
        # For now, return mock responses
        if model == "gpt-image-1":
            return {
                "output": "https://placehold.co/600x400?text=AI+Generated+Image",
                "type": "image",
                "model_used": "gpt-image-1"
            }
        elif model == "veo2":
            return {
                "output": "https://placehold.co/600x400/mp4?text=AI+Generated+Video",
                "type": "video",
                "model_used": "veo2"
            }
        elif model == "beatoven":
            # Generate music using Beatoven.ai
            topic = request.learning_topic or "general learning"
            music_url = generate_music(
                genre=request.genre,
                duration=request.duration,
                topic=topic
            )
            return {
                "output": music_url,
                "type": "music",
                "model_used": "beatoven"
            }
        else:  # Text models (gemini or o4-mini)
            # In a real implementation, we would use the appropriate API key
            api_key = OPENAI_API_KEY if model == "o4-mini" else GOOGLE_API_KEY
            return {
                "output": f"AI Response via {model}: " + request.input,
                "type": "text",
                "model_used": model
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run("main:app", host=host, port=port, reload=True)