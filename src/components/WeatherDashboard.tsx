import { useState } from "react";
import { WeatherSearch } from "./WeatherSearch";
import { WeatherCard } from "./WeatherCard";
import { ForecastCard } from "./ForecastCard";
import { useToast } from "@/hooks/use-toast";
import { weatherApi, WeatherData, ForecastDay } from "@/services/weatherApi";

export const WeatherDashboard = () => {
  const [currentWeather, setCurrentWeather] = useState<WeatherData | null>(null);
  const [forecast, setForecast] = useState<ForecastDay[]>([]);
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  // Real API call to our Python backend
  const fetchWeatherData = async (city: string) => {
    setLoading(true);
    
    try {
      // Fetch both current weather and forecast from our backend
      const { current, forecast } = await weatherApi.getWeatherAndForecast(city);
      
      setCurrentWeather(current);
      setForecast(forecast);
      
      toast({
        title: "Weather data loaded",
        description: `Successfully loaded weather for ${city}`,
      });
    } catch (error) {
      console.error("Weather API error:", error);
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to fetch weather data. Please try again.",
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-sky-gradient">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl md:text-6xl font-bold text-white mb-4 animate-fade-in">
            Weather Dashboard
          </h1>
          <p className="text-xl text-white/80 animate-fade-in">
            Get real-time weather information for any city
          </p>
        </div>

        {/* Search */}
        <div className="mb-8 animate-slide-up">
          <WeatherSearch onSearch={fetchWeatherData} loading={loading} />
        </div>

        {/* Weather Data */}
        {currentWeather && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <WeatherCard weather={currentWeather} />
            </div>
            <div>
              <ForecastCard forecast={forecast} />
            </div>
          </div>
        )}

        {/* Empty State */}
        {!currentWeather && !loading && (
          <div className="text-center py-16 animate-fade-in">
            <div className="text-white/60 text-lg">
              Search for a city to see the weather forecast
            </div>
          </div>
        )}
      </div>
    </div>
  );
};