import { Card } from "@/components/ui/card";
import { Cloud, Sun, CloudRain, CloudSnow } from "lucide-react";

interface ForecastDay {
  date: string;
  day: string;
  high: number;
  low: number;
  condition: string;
  description: string;
}

interface ForecastCardProps {
  forecast: ForecastDay[];
}

const getWeatherIcon = (condition: string, size: string = "h-8 w-8") => {
  switch (condition.toLowerCase()) {
    case 'clear':
    case 'sunny':
      return <Sun className={`${size} text-yellow-400`} />;
    case 'clouds':
    case 'cloudy':
      return <Cloud className={`${size} text-gray-400`} />;
    case 'rain':
    case 'drizzle':
      return <CloudRain className={`${size} text-blue-400`} />;
    case 'snow':
      return <CloudSnow className={`${size} text-blue-200`} />;
    default:
      return <Sun className={`${size} text-yellow-400`} />;
  }
};

export const ForecastCard = ({ forecast }: ForecastCardProps) => {
  return (
    <Card className="p-6 bg-card shadow-weather-card hover:shadow-weather-card-hover transition-all duration-300 animate-slide-up">
      <h3 className="text-xl font-semibold mb-4 text-card-foreground">5-Day Forecast</h3>
      
      <div className="space-y-4">
        {forecast.map((day, index) => (
          <div 
            key={day.date}
            className="flex items-center justify-between p-3 bg-secondary rounded-lg hover:bg-accent/50 transition-colors duration-200"
            style={{ animationDelay: `${index * 100}ms` }}
          >
            <div className="flex items-center space-x-4">
              {getWeatherIcon(day.condition)}
              <div>
                <p className="font-medium text-card-foreground">{day.day}</p>
                <p className="text-sm text-muted-foreground capitalize">{day.description}</p>
              </div>
            </div>
            
            <div className="text-right">
              <div className="flex items-center space-x-2">
                <span className="font-semibold text-lg text-card-foreground">
                  {Math.round(day.high)}°
                </span>
                <span className="text-muted-foreground">
                  {Math.round(day.low)}°
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
};