from src.functions import *
import threading
import time

def run_threads(num_letters=10000000, num_numbers=10000000):
    num_letters //= 2
    num_numbers //= 2
    
    total_start_time = time.time()

    # Shared lists to store thread results
    letter_results = [None, None]
    number_results = [None, None]

    # Wrapper functions to store results
    def run_join_letters(index, num):
        letter_results[index] = join_random_letters(num)

    def run_add_numbers(index, num):
        number_results[index] = add_random_numbers(num)

    # Create threads for both functions
    thread_letters1 = threading.Thread(target=run_join_letters, args=(0, num_letters))
    thread_letters2 = threading.Thread(target=run_join_letters, args=(1, num_letters))
    thread_numbers1 = threading.Thread(target=run_add_numbers, args=(0, num_numbers))
    thread_numbers2 = threading.Thread(target=run_add_numbers, args=(1, num_numbers))

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

    print(f"Total time taken: {total_end_time - total_start_time} seconds")



