from src.functions import *
import multiprocessing
import time

def run_processes(num_letters=10000000, num_numbers=10000000):
    num_letters //= 2
    num_numbers //= 2
    
    total_start_time = time.time()

    # Create a multiprocessing Manager to store results
    manager = multiprocessing.Manager()
    letter_results = manager.list([None, None])
    number_results = manager.list([None, None])

    # Wrapper functions to store results
    def run_join_letters(index, num, results):
        results[index] = join_random_letters(num)

    def run_add_numbers(index, num, results):
        results[index] = add_random_numbers(num)

    # Create processes for both functions
    process_letters1 = multiprocessing.Process(target=run_join_letters, args=(0, num_letters, letter_results))
    process_letters2 = multiprocessing.Process(target=run_join_letters, args=(1, num_letters, letter_results))
    process_numbers1 = multiprocessing.Process(target=run_add_numbers, args=(0, num_numbers, number_results))
    process_numbers2 = multiprocessing.Process(target=run_add_numbers, args=(1, num_numbers, number_results))

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


