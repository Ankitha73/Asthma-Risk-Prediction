import time
import board
import adafruit_dht
import requests
import pandas as pd
import joblib

# Load trained model
model = joblib.load("risk_model.pkl")

# DHT22 setup
dhtDevice = adafruit_dht.DHT22(board.D4)

# OpenWeather API Key
API_KEY = "7eb2bc2d110a47427c345aa2fd053166"

# Location coordinates
lat = 13.3409
lon = 74.7421

while True:
    try:
        # Read sensor data
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        # AQI API URL
        aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

        # Get AQI data
        aqi_response = requests.get(aqi_url)
        aqi_data = aqi_response.json()

        # Extract AQI value
        aqi = aqi_data['list'][0]['main']['aqi']

        # Prepare ML input
        input_data = pd.DataFrame(
            [[temperature, humidity, aqi]],
            columns=['temperature', 'humidity', 'aqi']
        )

        # Predict risk
        prediction = model.predict(input_data)

        # Print output
        print("Temperature:", temperature)
        print("Humidity:", humidity)
        print("AQI:", aqi)
        print("Predicted Risk:", prediction[0])
        print("--------------------------------")

    except RuntimeError as error:
        print(error.args[0])

    except Exception as e:
        print("Error:", e)

    time.sleep(5)