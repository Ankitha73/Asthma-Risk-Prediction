import requests

# Paste your OpenWeather API key here
API_KEY = "7eb2bc2d110a47427c345aa2fd053166"

# City name
city = "Bangalore"

# Step 1: Get latitude and longitude
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(weather_url)

data = response.json()

lat = data['coord']['lat']
lon = data['coord']['lon']

print("Latitude:", lat)
print("Longitude:", lon)

# Step 2: Get AQI data
aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

aqi_response = requests.get(aqi_url)

aqi_data = aqi_response.json()

# Extract AQI value
aqi = aqi_data['list'][0]['main']['aqi']

# Print AQI value
print("AQI Value:", aqi)

# Print full AQI data (optional)
print(aqi_data)