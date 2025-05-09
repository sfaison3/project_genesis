from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

def mount_static_files(app: FastAPI):
    # Add CORS middleware to allow the frontend to call the API
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # For development - modify for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Create images directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")
        print("Created images directory")
    
    # Mount the images directory
    app.mount("/images", StaticFiles(directory="images"), name="images")
    
    # Debug helper - list all directories and files
    print("\n=== DEBUG: Listing available files ===")
    os.system("ls -la ./")
    os.system("ls -la ./images/ || echo 'No images found'")
    print("=== End directory listing ===\n")
    
    @app.get("/api/health")
    async def health_check():
        return {"status": "ok"}