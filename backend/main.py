from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import os
from dotenv import load_dotenv
from typing import Optional, List
import logging
from datetime import datetime, timedelta
import json
from services.weather_service import WeatherService

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Weather Dashboard API",
    description="Backend API for the Weather Dashboard application",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:5173").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

# Simple in-memory cache (replace with Redis in production)
weather_cache = {}
weather_service = WeatherService()

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Weather Dashboard API", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/weather/current")
async def get_current_weather(
    city: str = Query(..., description="City name"),
    country_code: Optional[str] = Query(None, description="Country code (e.g., US, GB)")
):
    """Get current weather for a city"""
    try:
        # Check cache first
        cache_key = f"current_{city}_{country_code or 'default'}"
        if cache_key in weather_cache:
            cached_data = weather_cache[cache_key]
            if datetime.now() - cached_data["timestamp"] < timedelta(minutes=10):
                logger.info(f"Returning cached weather data for {city}")
                return cached_data["data"]

        if not OPENWEATHER_API_KEY:
            raise HTTPException(status_code=500, detail="OpenWeather API key not configured")

        weather_data = await weather_service.get_current_weather(city, country_code)

        # Cache the result
        weather_cache[cache_key] = {
            "data": weather_data,
            "timestamp": datetime.now()
        }

        logger.info(f"Successfully fetched weather for {city}")
        return weather_data

    except HTTPException:
        raise
    except ValueError as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/weather/forecast")
async def get_weather_forecast(
    city: str = Query(..., description="City name"),
    country_code: Optional[str] = Query(None, description="Country code (e.g., US, GB)")
):
    """Get 5-day weather forecast for a city"""
    try:
        # Check cache first
        cache_key = f"forecast_{city}_{country_code or 'default'}"
        if cache_key in weather_cache:
            cached_data = weather_cache[cache_key]
            if datetime.now() - cached_data["timestamp"] < timedelta(minutes=30):
                logger.info(f"Returning cached forecast data for {city}")
                return cached_data["data"]

        if not OPENWEATHER_API_KEY:
            raise HTTPException(status_code=500, detail="OpenWeather API key not configured")

        forecast_data = await weather_service.get_forecast(city, country_code)

        # Cache the result
        weather_cache[cache_key] = {
            "data": forecast_data,
            "timestamp": datetime.now()
        }

        logger.info(f"Successfully fetched forecast for {city}")
        return forecast_data

    except HTTPException:
        raise
    except ValueError as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/weather/search")
async def search_cities(
    query: str = Query(..., description="City search query"),
    limit: int = Query(5, ge=1, le=10, description="Maximum number of results")
):
    """Search for cities by name"""
    try:
        if not OPENWEATHER_API_KEY:
            raise HTTPException(status_code=500, detail="OpenWeather API key not configured")

        # Use OpenWeather's geocoding API for city search
        params = {
            "q": query,
            "limit": limit,
            "appid": OPENWEATHER_API_KEY
        }

        async with httpx.AsyncClient() as client:
            response = await client.get("http://api.openweathermap.org/geo/1.0/direct", params=params)
            response.raise_for_status()
            
            cities = response.json()
            
            results = []
            for city in cities:
                results.append({
                    "name": city["name"],
                    "country": city["country"],
                    "state": city.get("state"),
                    "lat": city["lat"],
                    "lon": city["lon"]
                })

            logger.info(f"City search for '{query}' returned {len(results)} results")
            return results

    except httpx.HTTPStatusError as e:
        logger.error(f"OpenWeather geocoding API error: {e}")
        raise HTTPException(status_code=500, detail="City search service unavailable")
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    
    if not OPENWEATHER_API_KEY:
        logger.warning("OpenWeather API key not found. Please set OPENWEATHER_API_KEY environment variable.")
    
    uvicorn.run(
        "main:app",
        host=os.getenv("BACKEND_HOST", "0.0.0.0"),
        port=int(os.getenv("BACKEND_PORT", 8000)),
        reload=True
    )
