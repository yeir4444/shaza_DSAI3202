import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from src.function3 import *
from src.function4 import *

def main3():
    sizes = [10**5, 10**6] 
    for size in sizes:
        numbers = [random.randint(1, 5) for _ in range(size)]
        print(f"Testing with {size} numbers:")

        start = time.time()
        sequential_square(numbers)
        print("Sequential:", time.time() - start)

        start = time.time()
        multiprocessing_square(numbers)
        print("Multiprocessing (one process per number):", time.time() - start)

        start = time.time()
        multiprocessing_pool_map(numbers)
        print("Multiprocessing Pool (map):", time.time() - start)

        start = time.time()
        process_pool_executor(numbers)
        print("ProcessPoolExecutor:", time.time() - start)
        
        print("--------------------")

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
