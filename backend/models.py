from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class WeatherData(BaseModel):
    """Current weather data model"""
    city: str = Field(..., description="City name")
    country: str = Field(..., description="Country code")
    temperature: int = Field(..., description="Temperature in Celsius")
    condition: str = Field(..., description="Weather condition (e.g., clear, clouds, rain)")
    description: str = Field(..., description="Detailed weather description")
    humidity: int = Field(..., description="Humidity percentage")
    windSpeed: int = Field(..., description="Wind speed in km/h")
    visibility: int = Field(..., description="Visibility in km")
    feelsLike: int = Field(..., description="Feels like temperature in Celsius")
    pressure: Optional[int] = Field(None, description="Atmospheric pressure in hPa")
    sunrise: Optional[int] = Field(None, description="Sunrise timestamp")
    sunset: Optional[int] = Field(None, description="Sunset timestamp")
    timestamp: str = Field(..., description="Data timestamp")

class ForecastDay(BaseModel):
    """Daily forecast data model"""
    date: str = Field(..., description="Forecast date (YYYY-MM-DD)")
    day: str = Field(..., description="Day name")
    high: int = Field(..., description="High temperature in Celsius")
    low: int = Field(..., description="Low temperature in Celsius")
    condition: str = Field(..., description="Weather condition")
    description: str = Field(..., description="Weather description")

class CitySearchResult(BaseModel):
    """City search result model"""
    name: str = Field(..., description="City name")
    country: str = Field(..., description="Country code")
    state: Optional[str] = Field(None, description="State/province")
    lat: float = Field(..., description="Latitude")
    lon: float = Field(..., description="Longitude")

class WeatherResponse(BaseModel):
    """Standard weather API response"""
    success: bool = Field(..., description="Request success status")
    data: Optional[WeatherData] = Field(None, description="Weather data")
    error: Optional[str] = Field(None, description="Error message")
    timestamp: str = Field(..., description="Response timestamp")

class ForecastResponse(BaseModel):
    """Standard forecast API response"""
    success: bool = Field(..., description="Request success status")
    data: Optional[List[ForecastDay]] = Field(None, description="Forecast data")
    error: Optional[str] = Field(None, description="Error message")
    timestamp: str = Field(..., description="Response timestamp")

class CitySearchResponse(BaseModel):
    """Standard city search API response"""
    success: bool = Field(..., description="Request success status")
    data: Optional[List[CitySearchResult]] = Field(None, description="Search results")
    error: Optional[str] = Field(None, description="Error message")
    timestamp: str = Field(..., description="Response timestamp")

class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Check timestamp")
    version: str = Field(..., description="API version")
    uptime: Optional[float] = Field(None, description="Service uptime in seconds")
