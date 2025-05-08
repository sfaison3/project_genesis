#!/usr/bin/env python3
"""
Integration tests for the FastAPI Beatoven.ai endpoint
This runs against a local FastAPI server and tests the /api/music/generate endpoint
"""
import sys
import json
import requests
import time
import subprocess
import os
import signal
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_URL = "http://localhost:8000"
SERVER_PROCESS = None

def start_server():
    """Start the FastAPI server in the background"""
    global SERVER_PROCESS
    print("🚀 Starting FastAPI server...")
    
    # Start server as a subprocess
    SERVER_PROCESS = subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid  # So we can kill the process group later
    )
    
    # Wait for server to start
    time.sleep(3)
    
    # Check if server is running by pinging the health endpoint
    try:
        health_response = requests.get(f"{API_URL}/api/health")
        if health_response.status_code == 200:
            print("✅ Server started successfully!")
            return True
        else:
            print(f"❌ Server health check failed with status code {health_response.status_code}")
            stop_server()
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to server")
        stop_server()
        return False

def stop_server():
    """Stop the FastAPI server"""
    global SERVER_PROCESS
    if SERVER_PROCESS:
        print("🛑 Stopping FastAPI server...")
        try:
            # Kill the process group to ensure all child processes are terminated
            os.killpg(os.getpgid(SERVER_PROCESS.pid), signal.SIGTERM)
            SERVER_PROCESS.wait(timeout=5)
            print("✅ Server stopped successfully")
        except subprocess.TimeoutExpired:
            print("⚠️ Server did not stop gracefully, forcefully terminating...")
            os.killpg(os.getpgid(SERVER_PROCESS.pid), signal.SIGKILL)
        except Exception as e:
            print(f"⚠️ Error stopping server: {str(e)}")
        finally:
            SERVER_PROCESS = None

def test_music_genre_endpoint():
    """Test the /api/music/genres endpoint"""
    print("\n🔍 Testing /api/music/genres endpoint...")
    try:
        response = requests.get(f"{API_URL}/api/music/genres")
        if response.status_code == 200:
            genres = response.json()
            print(f"✅ Successfully retrieved {len(genres)} music genres")
            return genres
        else:
            print(f"❌ Failed to get music genres: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_music_generation_endpoint(genre, topic, custom_prompt=None, duration=60):
    """Test the /api/music/generate endpoint"""
    request_body = {
        "genre": genre,
        "topic": topic,
        "duration": duration
    }
    
    if custom_prompt:
        request_body["custom_prompt"] = custom_prompt
    
    print(f"\n🎵 Testing music generation: {genre} about {topic}")
    print(f"Request payload: {json.dumps(request_body, indent=2)}")
    
    try:
        response = requests.post(
            f"{API_URL}/api/music/generate", 
            json=request_body
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Music generation successful!")
            print(f"Output URL: {result.get('output_url')}")
            print(f"Prompt used: {result.get('prompt_used')}")
            return result
        else:
            print(f"❌ Music generation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_generate_endpoint_with_beatoven(topic, genre="hip_hop", duration=60):
    """Test the main /api/generate endpoint with Beatoven.ai model"""
    request_body = {
        "input": f"Create a song about {topic}",
        "model": "beatoven",
        "genre": genre,
        "duration": duration,
        "learning_topic": topic
    }
    
    print(f"\n🔄 Testing general /api/generate endpoint with Beatoven model")
    print(f"Request payload: {json.dumps(request_body, indent=2)}")
    
    try:
        response = requests.post(
            f"{API_URL}/api/generate", 
            json=request_body
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Generation successful!")
            print(f"Output: {result.get('output')}")
            print(f"Type: {result.get('type')}")
            print(f"Model used: {result.get('model_used')}")
            return result
        else:
            print(f"❌ Generation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {str(e)}")
        return None

def run_integration_tests():
    """Run all integration tests"""
    # Make sure the BEATOVEN_API_KEY is set
    if not os.getenv("BEATOVEN_API_KEY"):
        print("⚠️ WARNING: BEATOVEN_API_KEY environment variable is not set")
        print("Tests will run but actual Beatoven.ai API calls will fail")
    
    # Start the server
    if not start_server():
        print("❌ Cannot continue with tests as server failed to start")
        return
    
    try:
        # Test getting available genres
        test_music_genre_endpoint()
        
        # Test music generation with different genres
        test_cases = [
            {
                "genre": "hip_hop",
                "topic": "photosynthesis",
                "description": "Hip hop track about photosynthesis"
            },
            {
                "genre": "country",
                "topic": "American Revolution",
                "description": "Country song about the American Revolution"
            },
            {
                "genre": "hip_hop",
                "topic": "geometry",
                "custom_prompt": "Educational hip hop with math-inspired beats",
                "description": "Hip hop with custom prompt about geometry"
            }
        ]
        
        for test_case in test_cases:
            test_music_generation_endpoint(
                genre=test_case["genre"],
                topic=test_case["topic"],
                custom_prompt=test_case.get("custom_prompt")
            )
        
        # Test the main generate endpoint with Beatoven model
        test_generate_endpoint_with_beatoven(
            topic="solar system",
            genre="country"
        )
        
        print("\n✅ All tests completed!")
    finally:
        # Stop the server
        stop_server()

if __name__ == "__main__":
    run_integration_tests()