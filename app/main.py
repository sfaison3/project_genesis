from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Literal
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Genesis API", description="Multi-modal AI Orchestration Platform")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if API keys are available
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not found in environment variables")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not found in environment variables")

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
    model: Optional[str] = "auto"  # auto, gpt-image-1, veo2, gemini, o4-mini

class GenerateResponse(BaseModel):
    output: str
    type: Literal["text", "image", "video"]
    model_used: str

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
    elif len(input_text) > 100:  # Longer requests might be better for o4-mini
        return "o4-mini"
    else:
        return "gemini"  # Default

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
            {"id": "o4-mini", "provider": "OpenAI", "type": "text"}
        ]
    }

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
        
        # This would call the actual AI services in production
        # For now, return mock responses with API key indicators
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