from mpi4py import MPI
import time
from src.calculate_square import square  # Ensure this correctly computes squares from 1 to n

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initial parameters
n = int(1e6)  # Start small
max_n = int(1e10)  # Ensures compliance with 3.f
time_limit = 300  # 300 seconds
start_time = time.time()

highest_square = 0  # Tracks max square

while True:
    # Time check BEFORE computing
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        if rank == 0:
            print("[DEBUG] Time limit reached, exiting loop.")
        break  # Exit immediately

    if rank == 0:
        print(f"=== Iteration with n = {n}, Time Elapsed: {elapsed_time:.2f}s ===")

    # Distribute workload
    local_n = n // size
    start_idx = rank * local_n + 1
    end_idx = (rank + 1) * local_n if rank != size - 1 else n

    # Compute max square in local range
    max_local_square = max(square(i) for i in range(start_idx, end_idx + 1))

    # Time check BEFORE sending/receiving (prevents deadlocks)
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        print(f"[Rank {rank}] Exiting before send/recv to avoid deadlock.")
        break  # Exit before communication

    # Send max square to rank 0 (root)
    if rank != 0:
        comm.send(max_local_square, dest=0, tag=rank)
    else:
        # Rank 0 will receive from all other ranks and compute the maximum
        highest_square = max_local_square  # Initialize with rank 0's local max
        for i in range(1, size):
            max_from_other_rank = comm.recv(source=i, tag=i)
            highest_square = max(highest_square, max_from_other_rank)

        # Print current highest square
        print(f"Square of {n} : {highest_square}")

    # Time check AFTER sending/receiving (final safeguard)
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        print(f"[Rank {rank}] Exiting after send/recv.")
        break

    # Dynamically increase `n`, but stay within limit
    n = min(int(n * 1.1), max_n)

# Root process prints final results
if rank == 0:
    final_elapsed_time = time.time() - start_time
    print(f"=== FINAL RESULT ===\nHighest square reached in {final_elapsed_time:.2f}s: {highest_square}")
