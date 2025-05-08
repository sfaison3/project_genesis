#!/usr/bin/env python3
"""
Direct test for the music generation functionality.
This doesn't require starting a server.
"""
import os
import json
from dotenv import load_dotenv
from main import generate_music, generate_lyrics_for_topic

# Load environment variables
load_dotenv()

def test_generate_music():
    """Test the generate_music function directly"""
    print("Testing music generation...")
    
    # Make sure TEST_MODE is set
    os.environ["BEATOVEN_API_KEY"] = "TEST_MODE"
    
    # Test with different genres
    for genre in ["hip_hop", "country", "pop"]:
        print(f"\nTesting {genre} genre:")
        result = generate_music(
            genre=genre,
            duration=60,
            topic="photosynthesis",
            poll_for_completion=True
        )
        
        # Print the results
        print("Results:")
        print(f"  Preview URL: {result['preview_url']}")
        print(f"  Track ID: {result.get('track_id')}")
        print(f"  Title: {result.get('title')}")
        print(f"  Lyrics snippet: {result.get('lyrics', '')[:100]}...")

def test_lyrics_generation():
    """Test the lyrics generation function"""
    print("\nTesting lyrics generation...")
    
    # Test different combinations
    test_cases = [
        {"topic": "photosynthesis", "genre": "hip_hop"},
        {"topic": "American Revolution", "genre": "country"},
        {"topic": "geometry", "genre": "pop"}
    ]
    
    for case in test_cases:
        print(f"\nGenerating lyrics for {case['topic']} in {case['genre']} style:")
        lyrics = generate_lyrics_for_topic(case["topic"], case["genre"])
        # Print the first few lines
        print("\n".join(lyrics.strip().split("\n")[:5]) + "...")

if __name__ == "__main__":
    test_generate_music()
    test_lyrics_generation()