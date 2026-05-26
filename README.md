# DHT22 Sensor Interfacing with Raspberry Pi

## Project Overview
This project demonstrates the interfacing of a DHT22 temperature and humidity sensor with Raspberry Pi using Python.

The system collects real-time environmental data and displays temperature and humidity readings through the Raspberry Pi terminal.

---

## Hardware Used
- Raspberry Pi
- DHT22 Sensor
- Jumper Wires
- Power Supply

---

## Software Used
- Raspberry Pi OS
- Python 3
- Adafruit_DHT Library

---

## Sensor Connections

| DHT22 Pin | Raspberry Pi Pin |
|-----------|------------------|
| VCC       | 3.3V             |
| GND       | GND              |
| DATA      | GPIO4            |

---

## Python Code

```python
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22
pin = 4

print("DHT22 Sensor Reading.... Press Ctrl+C to stop.")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.1f} °C")
        print(f"Humidity: {humidity:.1f} %")
        print("----------------------")
    else:
        print("Failed to retrieve data")

    time.sleep(2)
```

---

## Output

The Raspberry Pi terminal continuously displays:
- Temperature values
- Humidity values
- Real-time sensor readings

---

## Future Scope
- Integration of PM2.5 sensor
- Gas sensor integration
- Air quality prediction
- IoT-based environmental monitoring
