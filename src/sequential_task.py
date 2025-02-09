from src.functions import *
import time

def run_sequential(num_letters=10000000, num_numbers=10000000):
    total_start_time = time.time()

    letters_result = join_random_letters(num_letters)  # Store the result
    numbers_result = add_random_numbers(num_numbers)  # Use correct variable

    total_end_time = time.time()

    print(f"Total time taken: {total_end_time - total_start_time} seconds")

