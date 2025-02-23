import random
import time
import threading
from collections import deque

temperature_averages = {}

temperature_queue = deque()

MAX_READINGS = 10

def simulate_sensor():
    while True:
        temp = random.randint(15, 40)
        
        temperature_queue.append(temp)
        
        print(f"Temperature reading: {temp}°C")
        
        time.sleep(1)

def process_temperatures():
    while True:
        if temperature_queue:
            avg_temp = sum(temperature_queue) / len(temperature_queue)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            temperature_averages[timestamp] = avg_temp
            
          
            print(f"Time: {timestamp}, Average Temperature: {avg_temp:.2f}°C")
    
        time.sleep(1)


def start_threads():
    sensor_thread = threading.Thread(target=simulate_sensor)
    sensor_thread.daemon = True
    sensor_thread.start()

    processing_thread = threading.Thread(target=process_temperatures)
    processing_thread.daemon = True 
    processing_thread.start()

def run_threads():
    start_threads()
    while True:
        time.sleep(1)
