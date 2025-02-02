from src.functions import *
import threading
import time
import random
import string

def run_threads(num_letters= 100000, num_numbers=100000):

    num_letters= 100000//2
    num_numbers=100000//2
    total_start_time = time.time()
    # Create threads for both functions
    thread_letters1 =threading.Thread(target=join_random_letters(num_letters))
    thread_letters2 =threading.Thread(target=join_random_letters(num_letters))
    thread_numbers1 =threading.Thread(target=add_random_numbers(num_numbers))
    thread_numbers2 =threading.Thread(target=add_random_numbers(num_numbers))
    # Start the threads
    thread_letters1.start()
    thread_letters2.start()
    
    thread_numbers1.start()
    thread_numbers2.start()
    # Wait for all threads to complete
    thread_letters1.join()
    thread_letters2.join()
    
    thread_numbers1.join()
    thread_numbers2.join()
    
    total_end_time = time.time()
    print(f"Total time taken: {total_end_time -total_start_time} seconds")
