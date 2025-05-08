# Testing the Beatoven.ai Music Generation

This document provides instructions for testing the music generation functionality that integrates with Beatoven.ai.

## Test Mode

The application supports a "TEST_MODE" that simulates responses from Beatoven.ai without requiring an actual API key. This is useful for development and testing purposes.

### Setting Up Test Mode

To enable test mode, set the `BEATOVEN_API_KEY` environment variable to "TEST_MODE" in your `.env` file:

```
BEATOVEN_API_KEY=TEST_MODE
```

## Testing Methods

There are several ways to test the music generation functionality:

### 1. Direct Testing with Python Script

Use the included Python script to test the music generation functionality directly:

```bash
cd /Users/abesapien1/asu/project_genesis/app
python3 test_music_generation.py
```

This script tests the `generate_music` and `generate_lyrics_for_topic` functions with different genres and topics.

### 2. Test with Browser Interface

A simple HTML interface is available for testing the API:

1. Start the FastAPI server:
   ```bash
   cd /Users/abesapien1/asu/project_genesis/app
   uvicorn main:app --reload
   ```

2. Open a web browser and navigate to:
   ```
   http://localhost:8000/test
   ```

3. Use the form to generate music with different topics, genres, and durations.

### 3. Test with API Endpoints Directly

You can test the API endpoints directly using curl or other HTTP clients:

```bash
# Test music generation
curl -X 'POST' \
  'http://localhost:8000/api/music/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "genre": "hip_hop",
  "duration": 60,
  "topic": "photosynthesis"
}'

# Test the main generate endpoint
curl -X 'POST' \
  'http://localhost:8000/api/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "Create a song about photosynthesis",
  "model": "beatoven",
  "genre": "hip_hop",
  "duration": 60,
  "learning_topic": "photosynthesis"
}'
```

## Frontend Integration

For testing with the full Vue.js frontend, make sure the backend API is running, then start the frontend:

```bash
cd /Users/abesapien1/asu/project_genesis/frontend
npm run dev
```

Navigate to the displayed URL (usually http://localhost:5173) and use the updated UI to generate music.

## Expected Output

When testing in TEST_MODE, you'll get:

1. A mock MP3 URL from an open sample source
2. Generated lyrics based on the topic and genre
3. A track title based on the learning topic
4. A mock track ID for reference

## Troubleshooting

- If you encounter CORS issues, ensure the CORS middleware in the FastAPI app is properly configured.
- Check the FastAPI logs for detailed error messages.
- Verify that the TEST_MODE environment variable is correctly set.