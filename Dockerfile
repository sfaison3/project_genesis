# Simpler approach - single stage build
FROM python:3.10-slim

WORKDIR /app

# Add Node.js repository and install Node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Verify Node.js and npm installation
RUN node --version && npm --version

# Copy frontend files
COPY frontend/ /app/frontend/

# Build the frontend
WORKDIR /app/frontend
RUN npm ci
RUN npm run build || (echo "Frontend build failed" && exit 1)

# Create static directories
WORKDIR /app
RUN mkdir -p /app/static
RUN mkdir -p /app/static/images
RUN mkdir -p /app/static/assets/images

# Copy built assets and public files
RUN cp -r /app/frontend/dist/* /app/static/
RUN cp -r /app/frontend/public/images /app/static/images/
RUN cp -r /app/frontend/public/images /app/static/assets/images/

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

    # Debug helper - list all directories and files in static folder
    print("\n=== DEBUG: Listing files in static directory ===")
    os.system("ls -la /app/static/")
    os.system("ls -la /app/static/images/")
    os.system("ls -la /app/static/assets/ || echo 'assets dir not found'")
    print("=== End directory listing ===\n")

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