# Fixing the "API Status: Disconnected" Issue

If your frontend is deployed successfully but shows "API Status: Disconnected", follow these steps:

## Option 1: Deploy Both Frontend and Backend on Render

The updated `render.yaml` file now includes configurations for both:
- The frontend static site (`genesis-frontend`)
- The backend API service (`genesis-backend`)

After deploying both services:
1. Get the URL of your backend service from the Render dashboard
2. Set the `VITE_API_URL` environment variable in your frontend service to point to this backend URL

## Option 2: Manual Environment Variable Configuration

If you're deploying only the frontend:

1. In the Render dashboard, navigate to your static site
2. Go to "Environment" tab
3. Add a new environment variable:
   - Key: `VITE_API_URL`
   - Value: Your backend API URL (e.g., `https://your-backend.onrender.com` or another hosting service)
4. Click "Save Changes" and trigger a new deployment

## Option 3: Local Testing with Frontend Deployed

If your backend is running locally:

1. Start your backend locally (`cd app && uvicorn main:app --reload`)
2. Create a tunnel to expose your local backend using ngrok:
   ```bash
   ngrok http 8000
   ```
3. Use the ngrok URL as your `VITE_API_URL` in the Render environment variables

## Troubleshooting

If you still see "API Status: Disconnected" after setting the environment variables:

1. Open your browser's developer tools (F12)
2. Check the Console tab for errors
3. Look for network requests to `/health` endpoint and see if they're failing
4. Verify that your backend API is running and accessible
5. Check for CORS issues - your backend needs to allow requests from your frontend domain

### Checking the Current API URL

Your frontend tries to connect to the API using the URL from `config.js`. The current configuration uses:

```javascript
apiUrl: import.meta.env.VITE_API_URL || '/api'
```

If `VITE_API_URL` is not set, it falls back to '/api', which only works when the frontend and backend are hosted at the same domain.

### Fixing CORS Issues

If your backend is separate from your frontend, you'll need to enable CORS in your FastAPI backend:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```