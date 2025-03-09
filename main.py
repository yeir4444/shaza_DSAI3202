from mpi4py import MPI
import time
from src.calculate_square import compute_squares  # Ensure this returns only a single max value

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initial parameters
n = int(1e6)  # Start small
time_limit = 300  # Stop after 300 seconds
start_time = time.time()

MAX_N = int(1e12)  # Prevent `n` from growing too large

highest_square = 0  # Global max square tracker

while True:
    local_n = n // size
    start_idx = rank * local_n
    end_idx = (rank + 1) * local_n if rank != size - 1 else n

    # Compute only the max square value (not storing full list)
    max_local_square = compute_squares(start_idx, end_idx)

    # Get the max square across all ranks efficiently
    highest_square = comm.allreduce(max_local_square, op=MPI.MAX)

    # Check elapsed time
    elapsed_time = time.time() - start_time

    # Debugging outputs to track progress
    if rank == 0:
        print(f"Iteration {n}, Elapsed Time: {elapsed_time:.2f} seconds")

    if elapsed_time >= time_limit:
        break  # Stop when reaching 300 seconds

    # Dynamically increase `n`, but prevent it from becoming too large
    n = min(int(n * 1.1), MAX_N)

# Final output (only rank 0 prints)
if rank == 0:
    print(f"Highest square reached within 300s: {highest_square}")
    print(f"Execution Time: {elapsed_time:.2f} seconds")
