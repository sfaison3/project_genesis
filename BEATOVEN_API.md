# Beatoven.ai Music Generation API

The Genesis Music Learning App now includes a dedicated endpoint for generating music using Beatoven.ai. This endpoint allows you to create custom educational songs in various genres, with predefined genre-specific prompts that help create the right mood and style for your learning content.

## Endpoints

### Generate Music
```
POST /api/music/generate
```

### Check Music Track Status
```
GET /api/music/track/{track_id}
```

### List Available Genres
```
GET /api/music/genres
```

## Generate Music Request Format

```json
{
  "genre": "hip_hop",        // Required: The genre of music to generate
  "duration": 60,            // Optional: Duration in seconds (default: 60)
  "topic": "photosynthesis", // Required: The educational topic for the song
  "custom_prompt": "..."     // Optional: Custom prompt override
}
```

If `custom_prompt` is not provided, the system will automatically select an appropriate prompt from predefined options for the given genre.

## Generate Music Response Format

```json
{
  "output_url": "https://example.com/music.mp3", // URL to the generated music
  "genre": "hip_hop",                           // The genre that was used
  "prompt_used": "...",                         // The prompt that was used for generation
  "track_id": "abc123",                         // The Beatoven.ai track ID (if available)
  "status": "processing"                        // Status of the track (processing or completed)
}
```

## Track Status Response Format

```json
{
  "track_id": "abc123",
  "status": "COMPLETED",                      // PENDING, PROCESSING, COMPLETED, FAILED, ERROR
  "preview_url": "https://example.com/music.mp3", // URL to the completed track (if available)
  "created_at": "2023-06-01T12:00:00Z",
  "updated_at": "2023-06-01T12:05:00Z"
}
```

## Asynchronous Music Generation Flow

The music generation process with Beatoven.ai is asynchronous:

1. Make a request to `/api/music/generate` to start the music generation process
2. The response will include a `track_id` and an `output_url`
3. If the music isn't ready immediately, the `status` will be "processing"
4. Poll the `/api/music/track/{track_id}` endpoint to check when the track is ready
5. When `status` is "COMPLETED", the `preview_url` will contain the link to the finished track

## Supported Genres with Predefined Prompts

### Hip Hop

The system includes 5 predefined prompts for Hip Hop, such as:

- "West Coast heatwave with booming 808s, funky synth bass, and distorted vocal chops — think Dr. Dre meets Travis Scott in 2025. Mood: Swagger, Dominance."
- "Old-school NYC boom bap with a modern twist — crunchy snares, jazzy horns, and lyrical storytelling energy. Mood: Hustle, Confidence."
- "Futuristic drill beat with icy synths, rapid hi-hat rolls, and cinematic FX — imagine Blade Runner meets Pop Smoke. Mood: Cold, Intense."

### Country

The system includes 5 predefined prompts for Country, such as:

- "Southern backroad anthem with stomping drums, dirty slide guitar, and an outlaw vibe — perfect for a bonfire brawl. Mood: Rowdy, Rebel."
- "Modern country-pop hit with upbeat acoustic strums, catchy hooks, and arena-sized choruses — made to belt in a pickup truck. Mood: Free, Wild."
- "Dark country trap with ominous Dobro slides, moody pads, and deep bass — Johnny Cash meets trap house. Mood: Mysterious, Menacing."

## Supported Genre Mappings

The API automatically maps genre names to Beatoven.ai's supported formats:

| Our Genre | Beatoven.ai Genre |
|-----------|------------------|
| hip_hop   | hip-hop          |
| country   | country          |
| pop       | pop              |
| rock      | rock             |
| jazz      | jazz             |
| classical | classical        |
| electronic| electronic       |
| folk      | acoustic         |

## Integration with Main API

This endpoint is also integrated with the main `/api/generate` endpoint. When you set the model to `beatoven` or when the MCP routing logic selects Beatoven.ai as the best model for your request, the system will use the same music generation logic, automatically selecting an appropriate prompt for the specified genre.

## Example Requests

### Generate Music
```bash
curl -X 'POST' \
  'http://localhost:8000/api/music/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "genre": "hip_hop",
  "duration": 120,
  "topic": "photosynthesis",
  "custom_prompt": "Educational hip hop beat with a science lab vibe, perfect for memorizing plant biology concepts"
}'
```

### Check Track Status
```bash
curl -X 'GET' \
  'http://localhost:8000/api/music/track/abc123' \
  -H 'accept: application/json'
```

### List Available Genres
```bash
curl -X 'GET' \
  'http://localhost:8000/api/music/genres' \
  -H 'accept: application/json'
```

## Environment Variables

The Beatoven.ai API requires an API key, which should be set in the environment:

```
BEATOVEN_API_KEY=your_api_key_here
```

## Testing the Integration

Two test scripts are provided for testing the Beatoven.ai integration:

1. `test_beatoven_integration.py` - Tests direct interaction with Beatoven.ai API
2. `test_fastapi_beatoven.py` - Tests the FastAPI endpoints for music generation

To run the tests:
```bash
cd app
python3 test_beatoven_integration.py
python3 test_fastapi_beatoven.py
```

## Future Improvements

- Add support for more genres with predefined prompts
- Implement caching of generated music to improve response times
- Add ability to specify mood separate from genre
- Support for generating lyrics alongside the music
- Implement webhook notifications when tracks are complete