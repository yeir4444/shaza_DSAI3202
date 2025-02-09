import time

def calculate_sum(n):
    return sum(range(1, n + 1))

def run_sequential():
    
    number = 1000000
    start_time = time.time()
    
    total_sum = calculate_sum(number)
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    print(f"The sum of all numbers from 1 to {number} is {total_sum}.")
    print(f"Execution time: {execution_time} seconds.")