#!/usr/bin/env python3
"""
Simple script to run the Weather Dashboard Backend
"""

import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Get configuration from environment
    host = os.getenv("BACKEND_HOST", "0.0.0.0")
    port = int(os.getenv("BACKEND_PORT", 8000))
    
    # Check if API key is configured
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("⚠️  Warning: OPENWEATHER_API_KEY not set!")
        print("   Please create a .env file with your OpenWeather API key")
        print("   You can get a free API key at: https://openweathermap.org/api")
        print()
    
    print(f"🚀 Starting Weather Dashboard Backend...")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   API Key: {'✅ Configured' if api_key else '❌ Not configured'}")
    print()
    print(f"📖 API Documentation: http://{host}:{port}/docs")
    print(f"🔍 Health Check: http://{host}:{port}/health")
    print()
    
    # Start the server
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
