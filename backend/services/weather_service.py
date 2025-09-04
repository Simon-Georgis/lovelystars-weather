import httpx
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import os

logger = logging.getLogger(__name__)

class WeatherService:
    """Service class for handling weather API interactions"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        
        if not self.api_key:
            logger.warning("OpenWeather API key not configured")
    
    async def get_current_weather(self, city: str, country_code: Optional[str] = None) -> Dict[str, Any]:
        """Fetch current weather for a city"""
        if not self.api_key:
            raise ValueError("OpenWeather API key not configured")
        
        params = {
            "q": f"{city},{country_code}" if country_code else city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/weather", params=params)
            response.raise_for_status()
            
            data = response.json()
            return self._transform_current_weather(data)
    
    async def get_forecast(self, city: str, country_code: Optional[str] = None) -> List[Dict[str, Any]]:
        """Fetch 5-day forecast for a city"""
        if not self.api_key:
            raise ValueError("OpenWeather API key not configured")
        
        params = {
            "q": f"{city},{country_code}" if country_code else city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/forecast", params=params)
            response.raise_for_status()
            
            data = response.json()
            return self._transform_forecast(data)
    
    async def search_cities(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search for cities by name"""
        if not self.api_key:
            raise ValueError("OpenWeather API key not configured")
        
        params = {
            "q": query,
            "limit": limit,
            "appid": self.api_key
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(self.geo_url, params=params)
            response.raise_for_status()
            
            cities = response.json()
            return self._transform_city_search(cities)
    
    def _transform_current_weather(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transform OpenWeather API response to our format"""
        try:
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "condition": data["weather"][0]["main"].lower(),
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "windSpeed": round(data["wind"]["speed"] * 3.6),  # Convert m/s to km/h
                "visibility": round(data.get("visibility", 10000) / 1000),  # Convert m to km
                "feelsLike": round(data["main"]["feels_like"]),
                "pressure": data["main"]["pressure"],
                "sunrise": data["sys"]["sunrise"],
                "sunset": data["sys"]["sunset"],
                "timestamp": datetime.now().isoformat()
            }
        except KeyError as e:
            logger.error(f"Missing key in weather data: {e}")
            raise ValueError(f"Invalid weather data format: missing {e}")
    
    def _transform_forecast(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Transform OpenWeather forecast response to our format"""
        try:
            daily_forecasts = {}
            
            for item in data["list"]:
                date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
                if date not in daily_forecasts:
                    daily_forecasts[date] = {
                        "temps": [],
                        "conditions": [],
                        "descriptions": []
                    }
                
                daily_forecasts[date]["temps"].append(item["main"]["temp"])
                daily_forecasts[date]["conditions"].append(item["weather"][0]["main"].lower())
                daily_forecasts[date]["descriptions"].append(item["weather"][0]["description"])
            
            # Transform to our forecast format
            forecast_data = []
            days = ["Today", "Tomorrow", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            for i, (date, forecast) in enumerate(list(daily_forecasts.items())[:5]):
                # Get most common condition and description
                condition = max(set(forecast["conditions"]), key=forecast["conditions"].count)
                description = max(set(forecast["descriptions"]), key=forecast["descriptions"].count)
                
                forecast_data.append({
                    "date": date,
                    "day": days[i] if i < len(days) else datetime.strptime(date, "%Y-%m-%d").strftime("%A"),
                    "high": round(max(forecast["temps"])),
                    "low": round(min(forecast["temps"])),
                    "condition": condition,
                    "description": description
                })
            
            return forecast_data
            
        except KeyError as e:
            logger.error(f"Missing key in forecast data: {e}")
            raise ValueError(f"Invalid forecast data format: missing {e}")
    
    def _transform_city_search(self, cities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Transform city search response to our format"""
        try:
            results = []
            for city in cities:
                results.append({
                    "name": city["name"],
                    "country": city["country"],
                    "state": city.get("state"),
                    "lat": city["lat"],
                    "lon": city["lon"]
                })
            return results
            
        except KeyError as e:
            logger.error(f"Missing key in city search data: {e}")
            raise ValueError(f"Invalid city search data format: missing {e}")
    
    def validate_api_key(self) -> bool:
        """Validate if the API key is configured and working"""
        if not self.api_key:
            return False
        
        # You could add a simple API call here to test the key
        return True
