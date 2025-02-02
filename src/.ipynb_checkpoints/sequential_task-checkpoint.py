from src.functions import *
import time
import random
import string
def run_sequential(num_letters= 100000, num_numbers=100000):
    total_start_time = time.time()
    join_random_letters(num_letters)
    add_random_numbers(num_letters)
    total_end_time = time.time()
    print(f"Total time taken: {total_end_time - total_start_time} seconds")