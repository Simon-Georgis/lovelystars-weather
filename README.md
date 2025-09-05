# 🌦️ Lovelystars Weather App

A weather dashboard application built with **FastAPI** (backend) and a modern frontend (JS/React/Vite).  
It fetches weather data from the **OpenWeather API** and displays current conditions + forecasts.

---

## 🚀 Live Deployment

The backend is hosted on **Render (free tier)**:

👉 (https://lovelystars-weather.onrender.com)

⚠️ Notes on free Render hosting:
- The free instance **sleeps after 15 minutes of inactivity**.
- When you first open it after being idle, the server may take **30–60 seconds to "cold start"**.
- To wake up the backend, visit the base URL above, or call the `/health` endpoint:
https://lovelystars-weather.onrender.com/health


- Once awake, your frontend will be able to fetch data normally.

---

## 🖥️ Running Locally (Windows)

### 1. Clone the Repository
```bash
git clone https://github.com/Simon-Georgis/lovelystars-weather.git
cd lovelystars-weather
2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt
4. Set Environment Variables
Create a .env file in the project root:


OPENWEATHER_API_KEY=your_openweather_api_key
CORS_ORIGINS=http://localhost:5173
Replace your_openweather_api_key with a valid API key from OpenWeather.

5. Run the Backend

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Backend will start at:


http://localhost:8000
Test endpoints in your browser:

http://localhost:8000/health

http://localhost:8000/weather/current?city=sydney

6. Run the Frontend (if included)
If the repo has a frontend folder (client/ or frontend/):


cd frontend
npm install
npm run dev
Frontend will start at:


http://localhost:5173
🌐 API Endpoints
GET /weather/current?city=sydney → Current weather

GET /weather/forecast?city=sydney → 5-day forecast

GET /weather/search?query=syd → Search for cities

GET /health → Health check

⚡ Troubleshooting
502 error on Render → Happens if the app doesn’t bind to the correct $PORT.
This project is already configured to use Render’s PORT env variable.

Slow first request → Normal on Render free tier (cold start).

404 errors → Make sure you’re using the correct route paths (/weather/...).
