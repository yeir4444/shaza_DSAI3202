

# DSAI 3202 – Parallel and Distributed Computing
## Lab 4: Temperature Monitoring System

### 1. Objectives:
The goal of this lab is to develop a Python program that simulates temperature readings from multiple sensors, processes these readings, calculates the average temperatures, and displays this information in real-time on the console. The lab also introduces concepts like **threading**, **synchronization**, and **thread-safe data transfer** using **Queue**.

### 2. Tools and Concepts:
- **Python**: The programming language used to implement the solution.
- **Threading**: Allows concurrent execution of tasks, enabling the simulation of multiple sensors and data processing in parallel.
- **Queue**: Used for thread-safe data transfer between threads.
- **Locks and Conditions**: Used for synchronization and communication between threads to ensure data integrity.

### 3. Tasks:
In this lab, you will perform the following tasks:

#### 3.a. Implement Sensor Simulation
- **Objective**: Write a function `simulate_sensor` that simulates temperature readings from multiple sensors.
- **Implementation**:
  - Use `random.randint(15, 40)` to generate random temperatures between 15°C and 40°C.
  - Update a global dictionary `latest_temperatures` every second with the readings from each sensor.

#### 3.b. Implement Data Processing
- **Objective**: Write a function `process_temperatures` that continuously calculates the average temperature from the readings placed in a queue.
- **Implementation**:
  - The function should retrieve sensor data from a queue and calculate the average temperature.
  - Update a global dictionary `temperature_averages` with the calculated averages.

#### 3.c. Integrate Threading
- **Objective**: Create threads for each call to `simulate_sensor` and `process_temperatures`.
- **Implementation**:
  - Use **daemon threads** for both sensor simulation and data processing functions.
  - Daemon threads allow the main program to exit without waiting for these threads to complete, as they run in the background.
  
#### 3.d. Implement Display Logic
- **Objective**: Implement the logic to display the current sensor readings and averages on the console.
- **Implementation**:
  - Write a function `initialize_display` to print the initial layout, such as:
    ```
    Current temperatures:
    Latest Temperatures: Sensor 0: --°C Sensor 1: --°C Sensor 2: --°C
    Sensor 1 Average: --°C
    Sensor 2 Average: --°C
    Sensor 3 Average: --°C
    ```
  - The display should refresh every 5 seconds without erasing the previous information. 
  - Create a function `update_display` to replace the `--` with the actual temperature readings and averages, updating the console without clearing the screen.

#### 3.e. Synchronize Data Access
- **Objective**: Synchronize access to shared data structures using locks and conditions.
- **Implementation**:
  - Use **RLock** (Reentrant Lock) to protect shared data structures like `latest_temperatures` and `temperature_averages`.
  - Use **Condition** to control the timing of updates, ensuring that the sensor data and averages are updated at the appropriate intervals.

#### 3.f. Finish Building the Main Program and Organize Files
- **Objective**: Structure the program logically by organizing it into multiple files.
- **Implementation**:
  - Put the functions `simulate_sensor`, `process_temperatures`, `initialize_display`, and `update_display` into a separate module (e.g., `sensor_functions.py`).
  - Create a main program file (e.g., `main.py`) to initialize the queue, share data structures, and manage the threads.
  - Start sensor threads and data processing threads, and initialize the console display update thread to refresh every 5 seconds.
  - Ensure the main thread remains active to allow daemon threads to operate in the background.

#### Bonus Task (5% in the Assignment):
- Modify the program so that:
  - The latest temperature readings are updated every 1 second.
  - The average temperatures are updated every 5 seconds, without erasing previous values in place.

### 4. Questions to be Answered in the README File:

1) **Which synchronization metric did you use for each of the tasks?**

   - **Sensor Simulation**: For sensor simulation, a **Condition** was used to control when to update the `latest_temperatures` dictionary. Since multiple threads may try to update the data concurrently, synchronization was necessary to ensure consistency.
   
   - **Data Processing**: An **RLock** (reentrant lock) was used to allow safe updating and reading of the `temperature_averages` dictionary. This lock is reentrant, meaning the same thread can acquire the lock multiple times, making it suitable for scenarios where the thread might need to access shared resources repeatedly.

   - **Display Updates**: A **Condition** was used to ensure that display updates occur at fixed intervals without interfering with sensor data collection or average calculations. This was important to keep the UI responsive and the data accurate.

2) **Why did the professor not ask you to compute metrics?**

   - The professor likely did not ask for the computation of metrics to focus on the core concepts of parallel programming, threading, and synchronization. The main objective of this lab was to simulate the sensors, process the data, and display the results in real-time while managing concurrency. By not asking for performance metrics, the lab emphasizes thread management and synchronization rather than performance optimization.

### 5. Conclusion:
This lab introduces fundamental concepts of parallel and distributed computing by simulating a temperature monitoring system using threading and synchronization techniques. The tasks simulate real-time data collection and processing with concurrent threads, ensuring thread-safe updates and periodic display refreshes. The assignment also emphasizes the practical application of **threading**, **queues**, **locks**, and **conditions** in Python for managing shared data and ensuring consistency in a concurrent environment.

### 6. Dependencies:
- **Python 3.x**: Required to run the program.
- **Threading**: A standard Python library for concurrent execution.
- **Queue**: A thread-safe data structure available in Python’s standard library.
  
