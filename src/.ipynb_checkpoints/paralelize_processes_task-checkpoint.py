import multiprocessing
import os
import time

def calculate_sum(start, end, result_file):
    total = sum(range(start, end + 1))
    with open(result_file, 'w') as f:
        f.write(str(total))
def run_processes():
    start_time = time.time()
    
    n = 1000000
    num_processes = 4
    step = n // num_processes
    
    processes = []
    
    for i in range(num_processes):
        start_process = (i * step) + 1
        end_process = (i + 1) * step if i != num_processes - 1 else n
        result_file = f'result_{i}.txt'
    
        process = multiprocessing.Process(target=calculate_sum, args=(start_process, end_process, result_file))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    results = []
    for i in range(num_processes):
        result_file = f'result_{i}.txt'
        with open(result_file, 'r') as f:
            results.append(int(f.read().strip()))
        os.remove(result_file)
    
    print(sum(results))
    end_time = time.time()
    print(f"All threads have finished, the execution time is {end_time - start_time}")
