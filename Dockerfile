# Multi-stage build for Genesis app
# Stage 1: Build frontend
FROM node:18-alpine AS frontend-build

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Build backend and combine with frontend
FROM python:3.10-slim

WORKDIR /app

# Copy built frontend assets
COPY --from=frontend-build /app/frontend/dist /app/static

# Ensure images directory exists and copy public images
RUN mkdir -p /app/static/images
COPY --from=frontend-build /app/frontend/public/images /app/static/images

# Also copy the images to assets directory for alternative references
RUN mkdir -p /app/static/assets/images
COPY --from=frontend-build /app/frontend/public/images /app/static/assets/images

# Install backend dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY app/ ./

# Copy root level files
COPY README.md CLAUDE.md ./

# Add static file serving
RUN pip install aiofiles

# Create script to start the service
RUN echo '#!/bin/bash\n\
python -m uvicorn main:app --host 0.0.0.0 --port $PORT\
' > /app/start.sh && chmod +x /app/start.sh

# Add code to serve static files
COPY <<'EOL' /app/static_files.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

def mount_static_files(app: FastAPI):
    # Mount static files from the frontend build
    app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

    # Explicitly mount the images directory
    app.mount("/images", StaticFiles(directory="static/images"), name="images")

    # Also serve images from assets directory
    app.mount("/assets/images", StaticFiles(directory="static/assets/images"), name="assets_images")

    @app.get("/")
    async def serve_frontend():
        return FileResponse("static/index.html")

    @app.get("/{path:path}")
    async def serve_frontend_paths(path: str):
        # Only serve known static files or fallback to index.html for SPA routing
        static_file = f"static/{path}"
        if os.path.exists(static_file) and os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")
EOL

# Modify main.py to include static file serving
RUN echo '\n# Import static file serving\nfrom static_files import mount_static_files\n# Mount static files\nmount_static_files(app)' >> main.py

# Set environment variables
ENV PORT=10000

# Expose the port
EXPOSE $PORT

# Start the app
CMD ["/app/start.sh"]