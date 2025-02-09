import threading
import time

def calculate_sum_for_threads(start: int = 1, end: int = 1000, results_list: list = []):
    result = 0
    for i in range(start, end + 1):
        result += i
    results_list.append(result)

def run_threads():
    
    start_time = time.time()
    
    n = 1000000
    num_threads = 4
    step = n // 4
    
    threads = []
    results = []
    
    for i in range(num_threads):
        start_thread = (i * step) + 1
        end_thread = (i + 1) * step
        thread = threading.Thread(target=calculate_sum_for_threads, args=(start_thread,end_thread,results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(sum(results))
    end_time = time.time()
    print(f"All threads have finished, the execution time is {end_time - start_time}")
