import { useState } from "react";
import { WeatherSearch } from "./WeatherSearch";
import { WeatherCard } from "./WeatherCard";
import { ForecastCard } from "./ForecastCard";
import { useToast } from "@/hooks/use-toast";

interface WeatherData {
  city: string;
  country: string;
  temperature: number;
  condition: string;
  description: string;
  humidity: number;
  windSpeed: number;
  visibility: number;
  feelsLike: number;
}

interface ForecastDay {
  date: string;
  day: string;
  high: number;
  low: number;
  condition: string;
  description: string;
}

export const WeatherDashboard = () => {
  const [currentWeather, setCurrentWeather] = useState<WeatherData | null>(null);
  const [forecast, setForecast] = useState<ForecastDay[]>([]);
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  // Mock API call - In a real app, you'd use OpenWeatherMap or similar API
  const fetchWeatherData = async (city: string) => {
    setLoading(true);
    
    try {
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Mock weather data - replace with real API call
      const mockWeatherData: WeatherData = {
        city: city,
        country: "Country",
        temperature: Math.round(Math.random() * 30 + 5), // 5-35°C
        condition: ["clear", "clouds", "rain"][Math.floor(Math.random() * 3)],
        description: "scattered clouds",
        humidity: Math.round(Math.random() * 40 + 40), // 40-80%
        windSpeed: Math.round(Math.random() * 20 + 5), // 5-25 km/h
        visibility: Math.round(Math.random() * 10 + 5), // 5-15 km
        feelsLike: Math.round(Math.random() * 30 + 5), // 5-35°C
      };

      const mockForecast: ForecastDay[] = [
        {
          date: "2024-01-01",
          day: "Today",
          high: mockWeatherData.temperature + Math.round(Math.random() * 5),
          low: mockWeatherData.temperature - Math.round(Math.random() * 5),
          condition: mockWeatherData.condition,
          description: mockWeatherData.description,
        },
        {
          date: "2024-01-02",
          day: "Tomorrow",
          high: Math.round(Math.random() * 30 + 5),
          low: Math.round(Math.random() * 15 + 0),
          condition: ["clear", "clouds", "rain"][Math.floor(Math.random() * 3)],
          description: "partly cloudy",
        },
        {
          date: "2024-01-03",
          day: "Wednesday",
          high: Math.round(Math.random() * 30 + 5),
          low: Math.round(Math.random() * 15 + 0),
          condition: ["clear", "clouds", "rain"][Math.floor(Math.random() * 3)],
          description: "sunny",
        },
        {
          date: "2024-01-04",
          day: "Thursday",
          high: Math.round(Math.random() * 30 + 5),
          low: Math.round(Math.random() * 15 + 0),
          condition: ["clear", "clouds", "rain"][Math.floor(Math.random() * 3)],
          description: "light rain",
        },
        {
          date: "2024-01-05",
          day: "Friday",
          high: Math.round(Math.random() * 30 + 5),
          low: Math.round(Math.random() * 15 + 0),
          condition: ["clear", "clouds", "rain"][Math.floor(Math.random() * 3)],
          description: "overcast",
        },
      ];

      setCurrentWeather(mockWeatherData);
      setForecast(mockForecast);
      
      toast({
        title: "Weather data loaded",
        description: `Successfully loaded weather for ${city}`,
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to fetch weather data. Please try again.",
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