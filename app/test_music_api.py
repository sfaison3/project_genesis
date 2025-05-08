#!/usr/bin/env python3
import sys
import json
import os
import random

# Mock the environment for testing
os.environ["BEATOVEN_API_KEY"] = "mock_key_for_testing"

from main import generate_music, GENRE_PROMPTS

def test_music_generation():
    """Test the music generation function with different genres"""
    
    # Test hip-hop genre
    print("\n--- Testing Hip Hop Genre ---")
    result = generate_music(
        genre="hip_hop", 
        duration=60, 
        topic="photosynthesis"
    )
    print(json.dumps(result, indent=2))
    
    # Test country genre
    print("\n--- Testing Country Genre ---")
    result = generate_music(
        genre="country", 
        duration=60, 
        topic="American Revolution"
    )
    print(json.dumps(result, indent=2))
    
    # Test with custom prompt
    print("\n--- Testing Custom Prompt ---")
    result = generate_music(
        genre="hip_hop", 
        duration=60, 
        topic="quantum physics",
        prompt="Bouncy trap beat with educational lyrics perfect for memorizing complex concepts"
    )
    print(json.dumps(result, indent=2))
    
    # Test genre not in predefined prompts
    print("\n--- Testing Genre Without Predefined Prompts ---")
    result = generate_music(
        genre="classical", 
        duration=90, 
        topic="ancient Greece"
    )
    print(json.dumps(result, indent=2))
    
    # Print all available genre prompts
    print("\n--- Available Genre Prompts ---")
    for genre, prompts in GENRE_PROMPTS.items():
        print(f"{genre.upper()}: {len(prompts)} prompt(s) available")
        for i, prompt in enumerate(prompts):
            print(f"  {i+1}. {prompt}")

if __name__ == "__main__":
    test_music_generation()