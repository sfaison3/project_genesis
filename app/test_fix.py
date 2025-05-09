"""
Test script to verify the fix for the educational_facts reference before assignment issue
"""
import sys
import os
# Add the parent directory to the path so we can import from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function we fixed
from app.main import generate_lyrics_for_topic

def test_wikipedia_integration():
    """Test the Wikipedia integration with various topics"""
    topics = [
        "Benjamin Franklin",
        "photosynthesis",
        "Napoleon Bonaparte",
        "World War II",
        "quantum physics"
    ]
    
    genres = ["hip_hop", "country", "rock", "electronic", "pop"]
    
    print("\n===== TESTING WIKIPEDIA INTEGRATION =====\n")
    
    for i, topic in enumerate(topics):
        genre = genres[i % len(genres)]
        print(f"\n----- Testing topic: '{topic}' with genre: '{genre}' -----\n")
        
        try:
            lyrics = generate_lyrics_for_topic(topic, genre)
            # Print a sample of the lyrics
            print(f"Generated lyrics (sample):")
            sample_lines = lyrics.strip().split("\n")[:10]
            for line in sample_lines:
                print(f"  {line}")
            print("  ...")
            print(f"  [Total lyrics length: {len(lyrics)} characters]")
            print("\n✅ SUCCESS: Generated lyrics without errors\n")
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n===== TEST COMPLETE =====\n")

if __name__ == "__main__":
    test_wikipedia_integration()