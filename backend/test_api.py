#!/usr/bin/env python3
"""
Simple test script to verify the Weather Dashboard Backend API
"""

import asyncio
import httpx
import json
from datetime import datetime

async def test_backend():
    """Test the backend API endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Weather Dashboard Backend API")
    print("=" * 50)
    
    async with httpx.AsyncClient() as client:
        # Test 1: Health check
        print("\n1. Testing health check...")
        try:
            response = await client.get(f"{base_url}/health")
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Health check passed: {data['status']}")
            else:
                print(f"   ❌ Health check failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Health check error: {e}")
        
        # Test 2: Root endpoint
        print("\n2. Testing root endpoint...")
        try:
            response = await client.get(f"{base_url}/")
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Root endpoint: {data['message']}")
            else:
                print(f"   ❌ Root endpoint failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Root endpoint error: {e}")
        
        # Test 3: Current weather (London)
        print("\n3. Testing current weather API...")
        try:
            response = await client.get(f"{base_url}/api/weather/current", params={"city": "London"})
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Current weather for London: {data['temperature']}°C, {data['condition']}")
            else:
                error_data = response.json()
                print(f"   ❌ Current weather failed: {error_data.get('detail', 'Unknown error')}")
        except Exception as e:
            print(f"   ❌ Current weather error: {e}")
        
        # Test 4: Forecast (London)
        print("\n4. Testing forecast API...")
        try:
            response = await client.get(f"{base_url}/api/weather/forecast", params={"city": "London"})
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Forecast for London: {len(data)} days")
                if data:
                    first_day = data[0]
                    print(f"      First day: {first_day['day']} - High: {first_day['high']}°C, Low: {first_day['low']}°C")
            else:
                error_data = response.json()
                print(f"   ❌ Forecast failed: {error_data.get('detail', 'Unknown error')}")
        except Exception as e:
            print(f"   ❌ Forecast error: {e}")
        
        # Test 5: City search
        print("\n5. Testing city search API...")
        try:
            response = await client.get(f"{base_url}/api/weather/search", params={"query": "lon", "limit": 3})
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ City search for 'lon': {len(data)} results")
                if data:
                    for city in data[:2]:  # Show first 2 results
                        print(f"      - {city['name']}, {city['country']}")
            else:
                error_data = response.json()
                print(f"   ❌ City search failed: {error_data.get('detail', 'Unknown error')}")
        except Exception as e:
            print(f"   ❌ City search error: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 API testing completed!")
    print("\n📖 API Documentation: http://localhost:8000/docs")
    print("🔍 Interactive testing: http://localhost:8000/docs")

if __name__ == "__main__":
    print("⚠️  Make sure the backend server is running on http://localhost:8000")
    print("   Start it with: python run.py")
    print()
    
    try:
        asyncio.run(test_backend())
    except KeyboardInterrupt:
        print("\n\n⏹️  Testing interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Testing failed: {e}")
        print("   Make sure the backend server is running and accessible")
