# Weather Dashboard Backend

A FastAPI-based backend service for the Weather Dashboard application that provides real-time weather data using the OpenWeatherMap API.

## Features

- 🌤️ **Current Weather**: Get real-time weather data for any city
- 📅 **5-Day Forecast**: Detailed weather predictions
- 🔍 **City Search**: Search for cities with autocomplete
- ⚡ **Fast Performance**: Built with FastAPI and async HTTP
- 🗄️ **Caching**: In-memory caching for better performance
- 📚 **Auto Documentation**: Interactive API docs with Swagger UI
- 🔒 **CORS Support**: Configured for frontend integration

## Prerequisites

- Python 3.8+
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Copy the example file
   cp env_example.txt .env
   
   # Edit .env and add your OpenWeather API key
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```

## Running the Backend

### Option 1: Using the run script
```bash
python run.py
```

### Option 2: Using uvicorn directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Using Python module
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Health Check
- `GET /` - Root endpoint
- `GET /health` - Health check

### Weather Data
- `GET /api/weather/current?city={city}&country_code={code}` - Current weather
- `GET /api/weather/forecast?city={city}&country_code={code}` - 5-day forecast
- `GET /api/weather/search?query={search}&limit={limit}` - City search

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Configuration

Environment variables in `.env`:

```env
# Required
OPENWEATHER_API_KEY=your_api_key_here

# Optional
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
LOG_LEVEL=INFO
```

## Frontend Integration

The backend is configured with CORS to work with your React frontend. Update your frontend to use these endpoints:

```typescript
// Example API calls
const API_BASE = 'http://localhost:8000/api';

// Get current weather
const weather = await fetch(`${API_BASE}/weather/current?city=London`);

// Get forecast
const forecast = await fetch(`${API_BASE}/weather/forecast?city=London`);

// Search cities
const cities = await fetch(`${API_BASE}/weather/search?query=lon&limit=5`);
```

## Development

### Project Structure
```
backend/
├── main.py              # FastAPI application
├── models.py            # Pydantic data models
├── services/            # Business logic
│   ├── __init__.py
│   └── weather_service.py
├── requirements.txt     # Python dependencies
├── run.py              # Run script
└── README.md           # This file
```

### Adding New Features

1. **New Endpoints**: Add to `main.py`
2. **Data Models**: Update `models.py`
3. **Business Logic**: Add to `services/` directory
4. **Dependencies**: Update `requirements.txt`

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure `OPENWEATHER_API_KEY` is set in `.env`
2. **Port Already in Use**: Change `BACKEND_PORT` in `.env` or kill the process using the port
3. **CORS Issues**: Check `CORS_ORIGINS` in `.env` includes your frontend URL

### Getting an OpenWeather API Key

1. Go to [openweathermap.org](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to "My API Keys"
4. Copy your API key
5. Add it to your `.env` file

## Production Deployment

For production, consider:

- Using Redis for caching instead of in-memory
- Adding authentication/rate limiting
- Using environment-specific configuration
- Setting up proper logging
- Using a production WSGI server like Gunicorn

## License

This project is part of the Weather Dashboard application.
