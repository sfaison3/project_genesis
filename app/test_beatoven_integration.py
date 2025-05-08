#!/usr/bin/env python3
"""
Integration tests for Beatoven.ai API endpoint
"""
import os
import sys
import json
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if we have the API key
BEATOVEN_API_KEY = os.getenv("BEATOVEN_API_KEY")
if not BEATOVEN_API_KEY:
    print("ERROR: BEATOVEN_API_KEY environment variable is not set")
    sys.exit(1)

# API Configuration
BASE_URL = "https://api.beatoven.ai/v1"
HEADERS = {
    "Authorization": f"Bearer {BEATOVEN_API_KEY}",
    "Content-Type": "application/json"
}

def test_beatoven_api_connection():
    """Test basic connection to Beatoven.ai API"""
    try:
        # Just a simple GET request to test authentication
        response = requests.get(f"{BASE_URL}/tracks", headers=HEADERS)
        response.raise_for_status()
        print("✅ Beatoven.ai API connection successful!")
        print(f"Response status: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Beatoven.ai API connection failed: {str(e)}")
        return False

def test_create_track(genre, prompt, duration=60, name="Test Track"):
    """Test creating a new track"""
    payload = {
        "name": name,
        "duration": duration,
        "genre": genre,
        "customPrompt": prompt
    }
    
    print(f"\n🎵 Creating {genre} track: \"{name}\"")
    print(f"Prompt: \"{prompt}\"")
    
    try:
        response = requests.post(f"{BASE_URL}/tracks", headers=HEADERS, json=payload)
        response.raise_for_status()
        track_data = response.json()
        track_id = track_data.get("id")
        
        print(f"✅ Track created successfully!")
        print(f"Track ID: {track_id}")
        
        if "previewUrl" in track_data and track_data["previewUrl"]:
            print(f"Preview URL: {track_data['previewUrl']}")
        else:
            print("No preview URL available yet - track may still be processing")
            
        return track_id, track_data
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to create track: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None, None

def test_get_track_status(track_id):
    """Test getting a track's status"""
    try:
        response = requests.get(f"{BASE_URL}/tracks/{track_id}", headers=HEADERS)
        response.raise_for_status()
        track_data = response.json()
        
        status = track_data.get("status", "unknown")
        print(f"Track status: {status}")
        
        if "previewUrl" in track_data and track_data["previewUrl"]:
            print(f"Preview URL: {track_data['previewUrl']}")
        
        return track_data
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to get track status: {str(e)}")
        return None

def test_wait_for_track_completion(track_id, timeout=300, interval=10):
    """Wait for track generation to complete"""
    print(f"\n⏳ Waiting for track {track_id} to complete (timeout: {timeout}s)...")
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        track_data = test_get_track_status(track_id)
        
        if not track_data:
            print("❌ Failed to get track status, aborting wait")
            return None
        
        status = track_data.get("status")
        
        if status == "COMPLETED":
            print(f"✅ Track completed successfully after {int(time.time() - start_time)} seconds!")
            return track_data
        elif status in ["FAILED", "ERROR"]:
            print(f"❌ Track generation failed with status: {status}")
            return track_data
        
        print(f"Current status: {status} (waiting {interval} seconds...)")
        time.sleep(interval)
    
    print(f"❌ Timed out after {timeout} seconds")
    return None

def run_integration_tests():
    """Run all integration tests"""
    print("🔍 Starting Beatoven.ai integration tests\n")
    
    # Test API connection
    if not test_beatoven_api_connection():
        print("Cannot continue with integration tests due to connection failure")
        return
    
    # Test creating tracks with different genres and prompts
    test_cases = [
        {
            "genre": "hip_hop",
            "prompt": "Educational West Coast heatwave with booming 808s, perfect for learning photosynthesis",
            "name": "Photosynthesis Lesson (Hip Hop)",
            "duration": 60
        },
        {
            "genre": "country", 
            "prompt": "Southern backroad anthem with stomping drums, explaining the American Revolution",
            "name": "American Revolution (Country)",
            "duration": 60
        }
    ]
    
    successful_tracks = []
    
    for test_case in test_cases:
        track_id, track_data = test_create_track(
            genre=test_case["genre"],
            prompt=test_case["prompt"],
            name=test_case["name"],
            duration=test_case["duration"]
        )
        
        if track_id:
            successful_tracks.append({"id": track_id, "data": track_data, "name": test_case["name"]})
    
    # Wait for track generation to complete
    for track in successful_tracks:
        complete_data = test_wait_for_track_completion(track["id"])
        if complete_data and complete_data.get("previewUrl"):
            print(f"\n✅ {track['name']} is ready at: {complete_data['previewUrl']}")
    
    print("\n🏁 Integration tests completed")

if __name__ == "__main__":
    run_integration_tests()