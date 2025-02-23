import random
import time

latest_temperatures = {}

def simulate_sensor():
    while True:
        temp = random.randint(15, 40)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())  # Current UTC timestamp
        latest_temperatures[timestamp] = temp
        
        print(f"Time: {timestamp}, Temperature: {temp}°C")
        time.sleep(1)

