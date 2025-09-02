import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Search, MapPin } from "lucide-react";

interface WeatherSearchProps {
  onSearch: (city: string) => void;
  loading?: boolean;
}

export const WeatherSearch = ({ onSearch, loading = false }: WeatherSearchProps) => {
  const [city, setCity] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (city.trim()) {
      onSearch(city.trim());
    }
  };

  return (
    <div className="w-full max-w-md mx-auto animate-fade-in">
      <form onSubmit={handleSubmit} className="flex gap-2">
        <div className="relative flex-1">
          <MapPin className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground h-4 w-4" />
          <Input
            type="text"
            placeholder="Enter city name..."
            value={city}
            onChange={(e) => setCity(e.target.value)}
            className="pl-10 h-12 text-lg bg-card border-border focus:ring-primary"
            disabled={loading}
          />
        </div>
        <Button 
          type="submit" 
          size="lg"
          disabled={loading || !city.trim()}
          className="h-12 px-6 bg-primary hover:bg-primary/90 text-primary-foreground"
        >
          {loading ? (
            <div className="animate-spin h-4 w-4 border-2 border-primary-foreground border-t-transparent rounded-full" />
          ) : (
            <Search className="h-4 w-4" />
          )}
        </Button>
      </form>
    </div>
  );
};