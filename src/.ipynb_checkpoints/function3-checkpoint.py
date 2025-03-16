import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

def sequential_square(numbers):
    return [square(n) for n in numbers]

def multiprocessing_square(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square, numbers, min(10000, len(numbers) // multiprocessing.cpu_count()))
    pool.close()
    pool.join()
    return result

def multiprocessing_pool_map(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square, numbers, min(10000, len(numbers) // multiprocessing.cpu_count()))
    pool.close()
    pool.join()
    return result

def process_pool_executor(numbers):
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        return list(executor.map(square, numbers))