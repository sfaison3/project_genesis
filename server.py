"""
Main server runner for the Genesis Music Learning API
"""
import os
import sys
import uvicorn
from app.main import app

if __name__ == "__main__":
    print("Starting Genesis Music Learning API server...")
    
    # Create static directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(__file__), "app", "static")
    os.makedirs(static_dir, exist_ok=True)
    
    # Get host and port from environment or use defaults
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    
    # Run the server
    print(f"Server running on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="info")