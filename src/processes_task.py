from src.functions import *
import multiprocessing
import time
import random
import string

def run_processes(num_letters= 10000000, num_numbers=10000000):
    num_letters= 10000000//2
    num_numbers=10000000//2
    total_start_time = time.time()
    # Create processes for both functions
    process_letters1 =multiprocessing.Process(target=join_random_letters(num_letters)) 
    process_letters2 =multiprocessing.Process(target=join_random_letters(num_letters)) 
    
    process_numbers1 =multiprocessing.Process(target=add_random_numbers(num_numbers))
    process_numbers2 =multiprocessing.Process(target=add_random_numbers(num_numbers))
    
    # Start the processes
    process_letters1.start() 
    process_letters2.start() 
    
    process_numbers1.start()
    process_numbers2.start()
    
    # Wait for all processes to complete
    process_letters1.join()
    process_letters2.join()
    
    process_numbers1.join()
    process_numbers2.join()
    
    total_end_time = time.time()
    print(f"Total time taken: {total_end_time - total_start_time} seconds")