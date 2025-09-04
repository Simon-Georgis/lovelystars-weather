# Welcome to your Lovable project

## Project info

**URL**: https://lovable.dev/projects/2b7ec249-3fb5-4fc0-9592-f5caad56c755

## 🌟 New: Python Backend Added!

This project now includes a **Python FastAPI backend** that provides real weather data instead of mock data!

### 🚀 Quick Start with Backend

1. **Get a free OpenWeather API key**:
   - Visit [openweathermap.org/api](https://openweathermap.org/api)
   - Sign up and get your free API key

2. **Start the backend**:
   ```bash
   # Windows
   start_backend.bat
   
   # macOS/Linux
   chmod +x start_backend.sh
   ./start_backend.sh
   ```

3. **Start the frontend**:
   ```bash
   npm run dev
   ```

The backend will run on `http://localhost:8000` and your frontend will automatically connect to it!

### 🔧 Backend Features

- **Real-time weather data** from OpenWeatherMap API
- **5-day weather forecasts**
- **City search with autocomplete**
- **Fast performance** with FastAPI
- **Auto-generated API docs** at `/docs`
- **CORS configured** for frontend integration

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/2b7ec249-3fb5-4fc0-9592-f5caad56c755) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

### Frontend
- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

### Backend
- Python 3.8+
- FastAPI
- OpenWeatherMap API
- Async HTTP with httpx
- Pydantic data validation

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/2b7ec249-3fb5-4fc0-9592-f5caad56c755) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/tips-tricks/custom-domain#step-by-step-guide)

## 📚 Backend Documentation

For detailed backend information, see [backend/README.md](backend/README.md)

## 🔑 Environment Setup

Create a `.env` file in the `backend/` directory:

```env
OPENWEATHER_API_KEY=your_api_key_here
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```
