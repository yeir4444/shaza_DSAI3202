import time
import random
import multiprocessing
import asyncio
from concurrent.futures import ProcessPoolExecutor

# Function to compute the square of a number
def square(n):
    return n * n

# Sequential execution using a for loop
def sequential_square(numbers):
    return [square(n) for n in numbers]

# Multiprocessing using Pool.map()
def multiprocessing_square(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square, numbers, min(10000, len(numbers) // multiprocessing.cpu_count()))
    return result

# Multiprocessing Pool using map
def multiprocessing_pool_map(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square, numbers, min(10000, len(numbers) // multiprocessing.cpu_count()))
    return result

# Multiprocessing Pool using apply (slower, applies function to each element one by one)
def multiprocessing_pool_apply(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = [pool.apply(square, args=(n,)) for n in numbers]
    return results

# Using concurrent.futures ProcessPoolExecutor
def process_pool_executor(numbers):
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        return list(executor.map(square, numbers))

# Asynchronous function to compute squares
async def async_square(n):
    return await asyncio.to_thread(square, n)

# Asynchronous ProcessPoolExecutor using asyncio
async def async_process_pool_map(numbers):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = await loop.run_in_executor(executor, multiprocessing_pool_map, numbers)
    return results

# Function to time and execute a given function
def benchmark(func, numbers, label):
    start = time.time()
    func(numbers)
    end = time.time()
    print(f"{label}: {end - start:.4f} seconds")

# Function to time and execute an async function
async def async_benchmark(func, numbers, label):
    start = time.time()
    await func(numbers)
    end = time.time()
    print(f"{label}: {end - start:.4f} seconds")