import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print("Temperature:", temperature)
        print("Humidity:", humidity)
        print("-------------------")

    except RuntimeError as error:
        print(error.args[0])

    time.sleep(2)