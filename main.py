import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from src.function3 import *
from src.function4 import *

def main3():
    N1 = 10**6
    N2 = 10**7 
    numbers1 = [random.randint(1, 10) for _ in range(N1)]
    numbers2 = [random.randint(1, 10) for _ in range(N2)]

    for numbers, label in zip([numbers1, numbers2], ["1000000 numbers", "10000000 numbers"]):
        print(f"\nTesting with {label}:")

        benchmark(sequential_square, numbers, "Sequential")
        benchmark(multiprocessing_square, numbers, "Multiprocessing Pool (map)")
        benchmark(multiprocessing_pool_map, numbers, "Multiprocessing Pool (map)")
        benchmark(multiprocessing_pool_apply, numbers, "Multiprocessing Pool (apply)")
        benchmark(process_pool_executor, numbers, "ProcessPoolExecutor")

        # Run the async benchmark
        asyncio.run(async_benchmark(async_process_pool_map, numbers, "Asynchronous ProcessPoolExecutor"))

def main4():
    pool_size = 3  
    num_processes = 6  
    pool = ConnectionPool(pool_size)
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(target=access_database, args=(pool, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main4()
