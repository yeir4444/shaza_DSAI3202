from src.sensor_simulation import *
from src.data_processing import *
from src.integrate_threading import *
import time
import random
import string

# def performance_analysis():

#     num_threads = 6 
#     num_processes = 6
#     P = 0.9 

#     # Measure execution times
#     print("Running Sequential Execution...")
#     start = time.time()
#     run_sequential()
#     T_sequential = time.time() - start

#     print("\nRunning Threading Execution...")
#     start = time.time()
#     run_threads()
#     T_threads = time.time() - start

#     print("\nRunning Multiprocessing Execution...")
#     start = time.time()
#     run_processes()
#     T_processes = time.time() - start

#     # Compute Speedups
#     S_threads = T_sequential / T_threads
#     S_processes = T_sequential / T_processes

#     # Compute Efficiencies
#     E_threads = S_threads / num_threads
#     E_processes = S_processes / num_processes

#     # Compute Amdahl’s Speedup
#     S_A_threads = 1 / ((1 - P) + (P / num_threads))
#     S_A_processes = 1 / ((1 - P) + (P / num_processes))

#     # Compute Gustafson’s Speedup
#     S_G_threads = (1 - P) + (P * num_threads)
#     S_G_processes = (1 - P) + (P * num_processes)

#     # Print results
#     print("\n=== Performance Analysis Results ===")
#     print(f"Sequential Time: {T_sequential:.4f} sec")
#     print(f"Threading Time: {T_threads:.4f} sec, Speedup: {S_threads:.2f}, Efficiency: {E_threads:.2f}")
#     print(f"Multiprocessing Time: {T_processes:.4f} sec, Speedup: {S_processes:.2f}, Efficiency: {E_processes:.2f}")
#     print(f"Amdahl’s Law Speedup (Threads): {S_A_threads:.2f}")
#     print(f"Amdahl’s Law Speedup (Processes): {S_A_processes:.2f}")
#     print(f"Gustafson’s Law Speedup (Threads): {S_G_threads:.2f}")
#     print(f"Gustafson’s Law Speedup (Processes): {S_G_processes:.2f}")
    

# task 3_a: sequential
print("task 3_a: Implement Sensor Simulation")
simulate_sensor()

# task 3_b: processes
print("task 3_b: Implement Data Processing")
run_processes()

# task 3_c: threading
print("task 3_c: Integrate Threading")
run_threads()

# task 3_d: Performance analysis
print("task 3_d: Performance analysis")
run_threads()
