from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def compute_squares(start, end):
    return [i ** 2 for i in range(start, end)]

# Initial guess
n = int(1e7)  # Start small and increase
time_limit = 300  # 300 seconds
start_time = time.time()

while True:
    local_n = n // size
    start_idx = rank * local_n
    end_idx = (rank + 1) * local_n if rank != size - 1 else n

    local_squares = compute_squares(start_idx, end_idx)
    squares = comm.gather(local_squares, root=0)

    elapsed_time = time.time() - start_time

    if elapsed_time >= time_limit:
        break  # Stop when reaching 300 seconds

    n = int(n * 1.5)  # Increase n dynamically

if rank == 0:
    highest_square = (n - 1) ** 2
    print(f"Highest square reached within 300s: {highest_square}")
    print(f"Execution Time: {elapsed_time:.2f} seconds")
