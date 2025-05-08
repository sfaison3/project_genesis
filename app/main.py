from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Literal, List
import uvicorn
import os
import requests
import random
import time
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

# Music prompts by genre from CLAUDE.rules
HIP_HOP_PROMPTS = [
    "West Coast heatwave with booming 808s, funky synth bass, and distorted vocal chops — think Dr. Dre meets Travis Scott in 2025. Mood: Swagger, Dominance.",
    "Dark, cinematic trap beat layered with haunting strings, glitchy hi-hats, and bass drops that shake your bones. Mood: Gritty, Powerful.",
    "Old-school NYC boom bap with a modern twist — crunchy snares, jazzy horns, and lyrical storytelling energy. Mood: Hustle, Confidence.",
    "High-energy club banger with Afrobeat-influenced percussion, pitched-up vocal samples, and a beat drop that hits like a freight train. Mood: Party, Unstoppable.",
    "Futuristic drill beat with icy synths, rapid hi-hat rolls, and cinematic FX — imagine Blade Runner meets Pop Smoke. Mood: Cold, Intense."
]

COUNTRY_PROMPTS = [
    "Southern backroad anthem with stomping drums, dirty slide guitar, and an outlaw vibe — perfect for a bonfire brawl. Mood: Rowdy, Rebel.",
    "Modern country-pop hit with upbeat acoustic strums, catchy hooks, and arena-sized choruses — made to belt in a pickup truck. Mood: Free, Wild.",
    "Banjo-driven country rock with a pounding kick, electric guitar solos, and whiskey-fueled energy. Mood: Bold, Celebratory.",
    "High-octane bluegrass fusion with double-time fiddle riffs, foot-stomping rhythm, and explosive breakdowns. Mood: Fast, Fiery.",
    "Dark country trap with ominous Dobro slides, moody pads, and deep bass — Johnny Cash meets trap house. Mood: Mysterious, Menacing."
]

# Mapping genre to prompt lists
GENRE_PROMPTS = {
    "hip_hop": HIP_HOP_PROMPTS,
    "country": COUNTRY_PROMPTS
}

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
    type: str  # "text", "image", "video", "music"
    model_used: str
    title: Optional[str] = None
    lyrics: Optional[str] = None
    video_url: Optional[str] = None

class MusicGenreOption(BaseModel):
    id: str
    name: str
    description: str
    
class MusicGenerationRequest(BaseModel):
    genre: str
    duration: Optional[int] = 60  # Duration in seconds
    topic: str
    custom_prompt: Optional[str] = None  # Optional custom prompt, otherwise use predefined prompts

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

def generate_music(genre: str, duration: int, topic: str, prompt: str = None, poll_for_completion: bool = False):
    """Generate music using Beatoven.ai API"""
    # https://github.com/Beatoven/public-api/blob/main/docs/api-spec.md
    
    if not BEATOVEN_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Beatoven API key is required but not configured"
        )
    
    # Use provided prompt or get a random one from the genre-specific prompts
    music_prompt = prompt
    if not music_prompt and genre.lower() in GENRE_PROMPTS:
        music_prompt = random.choice(GENRE_PROMPTS[genre.lower()])
    
    track_name = f"Learning about {topic}"
    beatoven_genre = map_to_beatoven_genre(genre)
    
    # Get the track URL from Beatoven API
    preview_url = None
    track_id = None
    
    try:
        print(f"Creating track with Beatoven.ai: {genre} about {topic}")
        
        # Build the request payload for Beatoven API
        payload = {
            "name": track_name,
            "duration": duration,
            "genre": beatoven_genre,
            "customPrompt": music_prompt
        }
        
        # Make the API request
        response = requests.post(
            "https://api.beatoven.ai/v1/tracks",
            headers={"Authorization": f"Bearer {BEATOVEN_API_KEY}", "Content-Type": "application/json"},
            json=payload
        )
        
        if response.status_code != 200 and response.status_code != 201:
            print(f"Beatoven API error: {response.status_code} - {response.text}")
            # Fall back to placeholder in case of error
            return {
                "preview_url": f"https://placehold.co/400x100.mp3?text=AI+Music+{genre}+about+{topic}",
                "prompt_used": music_prompt or f"Default prompt for {genre}",
                "track_id": None,
                "title": track_name,
                "lyrics": f"Lyrics about {topic} in {genre} style would appear here."
            }
        
        data = response.json()
        track_id = data.get("id")
        print(f"Track created with ID: {track_id}")
        
        # Check if we have a preview URL immediately (unlikely but possible)
        preview_url = data.get("previewUrl")
        
        # If poll_for_completion is True, wait for the track to be ready
        if poll_for_completion and track_id:
            max_attempts = 10
            attempt = 0
            wait_time = 3  # Initial wait time in seconds
            
            while attempt < max_attempts and (not preview_url or not preview_url.endswith('.mp3')):
                print(f"Polling for track completion, attempt {attempt+1}/{max_attempts}")
                time.sleep(wait_time)
                
                # Exponential backoff - increase wait time gradually
                wait_time = min(wait_time * 1.5, 15)  # Cap at 15 seconds
                
                # Check track status
                try:
                    status_response = requests.get(
                        f"https://api.beatoven.ai/v1/tracks/{track_id}",
                        headers={"Authorization": f"Bearer {BEATOVEN_API_KEY}"}
                    )
                    
                    if status_response.status_code == 200:
                        track_data = status_response.json()
                        status = track_data.get("status")
                        preview_url = track_data.get("previewUrl")
                        
                        print(f"Track status: {status}, Preview URL: {preview_url}")
                        
                        if status == "COMPLETED" and preview_url and preview_url.endswith('.mp3'):
                            print("Track is ready!")
                            break
                        elif status in ["FAILED", "ERROR"]:
                            print(f"Track generation failed with status: {status}")
                            break
                    else:
                        print(f"Failed to get track status: {status_response.status_code}")
                
                except Exception as e:
                    print(f"Error checking track status: {str(e)}")
                
                attempt += 1
        
        # If no preview URL yet, use the track page URL
        if not preview_url:
            preview_url = f"https://app.beatoven.ai/track/{track_id}"
            print(f"Track is processing. You can check status at: {preview_url}")
            
        # If the URL isn't an MP3, try to get a direct download URL from the HTML page (not implemented here)
        if preview_url and not preview_url.endswith('.mp3'):
            print(f"Note: Preview URL is not a direct MP3 link: {preview_url}")
            
        # Generate lyrics about the topic (would come from an LLM in production)
        # This is a placeholder for now
        lyrics = generate_lyrics_for_topic(topic, genre)
        
    except Exception as e:
        print(f"Error calling Beatoven API: {str(e)}")
        # Fall back to placeholder in case of error
        return {
            "preview_url": f"https://placehold.co/400x100.mp3?text=AI+Music+{genre}+about+{topic}",
            "prompt_used": music_prompt or f"Default prompt for {genre}",
            "track_id": None,
            "title": track_name,
            "lyrics": f"Lyrics about {topic} in {genre} style would appear here."
        }
    
    return {
        "preview_url": preview_url,
        "prompt_used": music_prompt or f"Default prompt for {genre}",
        "track_id": track_id,
        "title": track_name,
        "lyrics": generate_lyrics_for_topic(topic, genre)
    }


def generate_lyrics_for_topic(topic: str, genre: str) -> str:
    """Generate lyrics for a given topic and genre.
    
    In a real implementation, this would call an LLM like OpenAI's o4-mini.
    For now, we'll return a simple template.
    """
    if genre.lower() == "hip_hop":
        return f"""
[Verse 1]
Listen up, let me tell you 'bout {topic}
Knowledge flowing, can't nobody stop it
Breaking it down so your mind can process
Learning new things, that's how we progress

[Chorus]
{topic.capitalize()}, yeah, that's what we're learning today
{topic.capitalize()}, understand it in a whole new way
{topic.capitalize()}, knowledge is the power we seek
{topic.capitalize()}, now you're at the learning peak

[Verse 2]
Don't just memorize, make sure you understand
This knowledge right here will help you expand
Your mind, your world, how you comprehend
With {topic} skills, there's no limit to where you can ascend
"""
    elif genre.lower() == "country":
        return f"""
[Verse 1]
Sitting here thinking 'bout {topic}
Like a sunrise over fields of grain
The lessons learned are never forgotten
Knowledge like rain after a summer drought

[Chorus]
Oh, {topic}
Teaching us about this world we're in
Oh, {topic}
Where learning and living begin

[Verse 2]
Take my hand, let's walk this road together
Understanding grows like wildflowers in spring
The wisdom of {topic} lasts forever
These are the lessons worth remembering
"""
    else:
        return f"""
[Verse]
Let me tell you about {topic}
A fascinating subject to explore
The more you learn, the more you grow
Understanding what it's all for

[Chorus]
{topic.capitalize()}, {topic.capitalize()}
Knowledge to help you on your way
{topic.capitalize()}, {topic.capitalize()}
Learning something new today
"""

def map_to_beatoven_genre(genre):
    """Maps our genre to Beatoven.ai supported genres"""
    # This is a simple mapping function - expand as needed
    genre_map = {
        "hip_hop": "hip-hop",
        "country": "country",
        "pop": "pop",
        "rock": "rock",
        "jazz": "jazz",
        "classical": "classical",
        "electronic": "electronic",
        "folk": "acoustic"
    }
    
    # Return mapped genre or the original if no mapping exists
    return genre_map.get(genre.lower(), genre)

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

class MusicGenerationResponse(BaseModel):
    output_url: str
    genre: str
    prompt_used: str
    track_id: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    lyrics: Optional[str] = None
    
@app.post("/api/music/generate", response_model=MusicGenerationResponse)
async def generate_music_endpoint(request: MusicGenerationRequest):
    """Generate music using Beatoven.ai with specified genre and prompt"""
    try:
        if not BEATOVEN_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="Beatoven API key is required but not configured"
            )
        
        # Use the generate_music function with polling enabled
        result = generate_music(
            genre=request.genre,
            duration=request.duration,
            topic=request.topic,
            prompt=request.custom_prompt,
            poll_for_completion=True  # Try to wait for the track to complete
        )
        
        # Extract track ID from URL if available and not already included
        track_id = result.get("track_id")
        if not track_id and "track/" in result["preview_url"]:
            track_id = result["preview_url"].split("track/")[-1]
        
        # Determine status based on URL type
        is_completed = result["preview_url"].endswith(".mp3")
        status = "completed" if is_completed else "processing"
        
        return {
            "output_url": result["preview_url"],
            "genre": request.genre,
            "prompt_used": result["prompt_used"],
            "track_id": track_id,
            "status": status,
            "title": result.get("title", f"Learning about {request.topic}"),
            "lyrics": result.get("lyrics", "Lyrics are being generated...")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/music/track/{track_id}")
async def get_track_status(track_id: str):
    """Get the status of a Beatoven.ai track"""
    if not BEATOVEN_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Beatoven API key is required but not configured"
        )
    
    try:
        # Call Beatoven API to get track status
        response = requests.get(
            f"https://api.beatoven.ai/v1/tracks/{track_id}",
            headers={"Authorization": f"Bearer {BEATOVEN_API_KEY}"}
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to get track status: {response.text}"
            )
        
        track_data = response.json()
        
        # Extract track name and genre for generating lyrics
        track_name = track_data.get("name", "")
        track_genre = track_data.get("genre", "")
        
        # Try to extract topic from track name
        topic = "general learning"
        if track_name.startswith("Learning about "):
            topic = track_name[len("Learning about "):]
        
        # Generate lyrics for the track
        lyrics = generate_lyrics_for_topic(topic, track_genre)
        
        # Check if track is completed and has a preview URL
        is_completed = track_data.get("status") == "COMPLETED"
        preview_url = track_data.get("previewUrl")
        
        return {
            "track_id": track_id,
            "status": track_data.get("status", "UNKNOWN"),
            "preview_url": preview_url,
            "created_at": track_data.get("createdAt"),
            "updated_at": track_data.get("updatedAt"),
            "title": track_name,
            "lyrics": lyrics,
            "is_ready": is_completed and preview_url and preview_url.endswith('.mp3')
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Beatoven API error: {str(e)}")

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
            music_result = generate_music(
                genre=request.genre,
                duration=request.duration,
                topic=topic,
                poll_for_completion=True  # Try to wait for the track to complete
            )
            
            # Create a more comprehensive response
            return {
                "output": music_result["preview_url"],
                "type": "music",
                "model_used": "beatoven",
                "title": music_result.get("title", f"Learning about {topic}"),
                "lyrics": music_result.get("lyrics", "Lyrics being generated..."),
                # We could add a video URL in the future
                "video_url": None
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