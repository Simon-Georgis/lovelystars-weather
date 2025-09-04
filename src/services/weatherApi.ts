const API_BASE = 'http://localhost:8000/api';

export interface WeatherData {
  city: string;
  country: string;
  temperature: number;
  condition: string;
  description: string;
  humidity: number;
  windSpeed: number;
  visibility: number;
  feelsLike: number;
  pressure?: number;
  sunrise?: number;
  sunset?: number;
  timestamp: string;
}

export interface ForecastDay {
  date: string;
  day: string;
  high: number;
  low: number;
  condition: string;
  description: string;
}

export interface CitySearchResult {
  name: string;
  country: string;
  state?: string;
  lat: number;
  lon: number;
}

class WeatherApiService {
  private async makeRequest<T>(endpoint: string, params?: Record<string, string>): Promise<T> {
    const url = new URL(`${API_BASE}${endpoint}`);
    
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        url.searchParams.append(key, value);
      });
    }

    const response = await fetch(url.toString());
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  async getCurrentWeather(city: string, countryCode?: string): Promise<WeatherData> {
    const params: Record<string, string> = { city };
    if (countryCode) {
      params.country_code = countryCode;
    }
    
    return this.makeRequest<WeatherData>('/weather/current', params);
  }

  async getForecast(city: string, countryCode?: string): Promise<ForecastDay[]> {
    const params: Record<string, string> = { city };
    if (countryCode) {
      params.country_code = countryCode;
    }
    
    return this.makeRequest<ForecastDay[]>('/weather/forecast', params);
  }

  async searchCities(query: string, limit: number = 5): Promise<CitySearchResult[]> {
    return this.makeRequest<CitySearchResult[]>('/weather/search', { 
      query, 
      limit: limit.toString() 
    });
  }

  async getWeatherAndForecast(city: string, countryCode?: string): Promise<{
    current: WeatherData;
    forecast: ForecastDay[];
  }> {
    const [current, forecast] = await Promise.all([
      this.getCurrentWeather(city, countryCode),
      this.getForecast(city, countryCode)
    ]);

    return { current, forecast };
  }
}

export const weatherApi = new WeatherApiService();
