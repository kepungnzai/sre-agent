"""
Serves as the application entry point. Initializes the FastAPI web server, 
discovers the agents defined in the workflow directory, and exposes them 
via HTTP endpoints for interaction.
"""
import uvicorn
import os
from pathlib import Path
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from dotenv import load_dotenv

# Load environment variables from .env file in the app directory
env_path = Path(__file__).parent / ".env"

print(f"Loading environment variables from: {env_path}")

load_dotenv(dotenv_path=env_path)

# Get the directory where main.py is located
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Configure the session service (e.g., SQLite for local storage)
SESSION_SERVICE_URI = "sqlite:///./sessions.db"

# Configure CORS to allow requests from various origins for this lab
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]

# Enable the ADK's built-in web interface
SERVE_WEB_INTERFACE = True

# Call the ADK function to discover agents and create the FastAPI app
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_SERVICE_URI,
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE,
)

if __name__ == "__main__":
    # Get the port from the PORT environment variable provided by the container runtime
    # Run the Uvicorn server, listening on all available network interfaces (0.0.0.0)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))