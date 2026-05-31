# Asthma Risk Prediction System

## Project Overview

This project is an IoT and Machine Learning based Asthma Risk Prediction System developed using Raspberry Pi.

The system collects:

* Temperature
* Humidity
* Air Quality Index (AQI)

using a DHT22 sensor and OpenWeather AQI API.

A Decision Tree Classifier machine learning algorithm is used to predict environmental asthma risk levels as:

* Low
* Medium
* High

---

## Features

* Real-time temperature monitoring
* Real-time humidity monitoring
* AQI monitoring using OpenWeather API
* Machine Learning based asthma risk prediction
* Raspberry Pi and IoT integration
* Environmental data analysis

---

## Technologies Used

* Raspberry Pi
* Python
* DHT22 Sensor
* OpenWeather AQI API
* Machine Learning
* Scikit-learn
* Pandas

---

## Machine Learning Algorithm Used

Decision Tree Classifier

---

## Files Included

* `dht22_read.py` → DHT22 sensor integration
* `aqi_test.py` → AQI API integration
* `train_model.py` → ML model training
* `live_prediction.py` → Final live prediction system
* `AirQuality.csv` → Dataset used for ML training
* `risk_model.pkl` → Trained ML model

---

## Hardware Components

* Raspberry Pi
* DHT22 Sensor
* Jumper Wires
* Breadboard
* WiFi Connection

---

## Output

The system predicts environmental asthma risk levels in real time using:

* Temperature
* Humidity
* AQI

Example Output:

Temperature: 31.4
Humidity: 71.3
AQI: 1
Predicted Risk: Medium

---

## Future Enhancements

Integration of PM2.5 and MQ135 gas sensors for advanced air quality monitoring.
Implementation of LCD display for local environmental status display.
Automatic air purifier control based on predicted risk levels.
Development of Generative AI-based health advisory and alert system.



