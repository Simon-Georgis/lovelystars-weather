import { Card } from "@/components/ui/card";
import { Cloud, Sun, CloudRain, CloudSnow, Wind, Eye, Droplets, Thermometer } from "lucide-react";

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

interface WeatherCardProps {
  weather: WeatherData;
}

const getWeatherIcon = (condition: string) => {
  const iconClass = "h-16 w-16 animate-float";
  
  switch (condition.toLowerCase()) {
    case 'clear':
    case 'sunny':
      return <Sun className={`${iconClass} text-yellow-400`} />;
    case 'clouds':
    case 'cloudy':
      return <Cloud className={`${iconClass} text-gray-400`} />;
    case 'rain':
    case 'drizzle':
      return <CloudRain className={`${iconClass} text-blue-400`} />;
    case 'snow':
      return <CloudSnow className={`${iconClass} text-blue-200`} />;
    default:
      return <Sun className={`${iconClass} text-yellow-400`} />;
  }
};

export const WeatherCard = ({ weather }: WeatherCardProps) => {
  return (
    <Card className="p-8 bg-card shadow-weather-card hover:shadow-weather-card-hover transition-all duration-300 animate-slide-up">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-3xl font-bold text-card-foreground">{weather.city}</h2>
          <p className="text-muted-foreground">{weather.country}</p>
        </div>
        <div className="text-right">
          {getWeatherIcon(weather.condition)}
        </div>
      </div>
      
      <div className="mb-6">
        <div className="flex items-baseline">
          <span className="text-6xl font-bold bg-temperature-gradient bg-clip-text text-transparent">
            {Math.round(weather.temperature)}
          </span>
          <span className="text-2xl text-muted-foreground ml-2">°C</span>
        </div>
        <p className="text-xl text-card-foreground capitalize">{weather.description}</p>
        <p className="text-muted-foreground">Feels like {Math.round(weather.feelsLike)}°C</p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="flex items-center space-x-3 p-3 bg-secondary rounded-lg">
          <Droplets className="h-5 w-5 text-blue-500" />
          <div>
            <p className="text-sm text-muted-foreground">Humidity</p>
            <p className="font-semibold">{weather.humidity}%</p>
          </div>
        </div>
        
        <div className="flex items-center space-x-3 p-3 bg-secondary rounded-lg">
          <Wind className="h-5 w-5 text-gray-500" />
          <div>
            <p className="text-sm text-muted-foreground">Wind Speed</p>
            <p className="font-semibold">{weather.windSpeed} km/h</p>
          </div>
        </div>
        
        <div className="flex items-center space-x-3 p-3 bg-secondary rounded-lg">
          <Eye className="h-5 w-5 text-purple-500" />
          <div>
            <p className="text-sm text-muted-foreground">Visibility</p>
            <p className="font-semibold">{weather.visibility} km</p>
          </div>
        </div>
        
        <div className="flex items-center space-x-3 p-3 bg-secondary rounded-lg">
          <Thermometer className="h-5 w-5 text-red-500" />
          <div>
            <p className="text-sm text-muted-foreground">Feels Like</p>
            <p className="font-semibold">{Math.round(weather.feelsLike)}°C</p>
          </div>
        </div>
      </div>
    </Card>
  );
};