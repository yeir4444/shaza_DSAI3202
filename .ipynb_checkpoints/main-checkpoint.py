from mpi4py import MPI
import numpy as np
from src.square import square


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"which prosses is this: {rank}, and size is:{size}")

if rank == 0:
    numbers= np.arange(size, dtype = "i")
    print(numbers)
else:
    numbers= None

number = np.zeros(1, dtype= "i")
comm.Scatter(numbers, number, root = 0)
print(number)

result = square(number[0])
print(result)

request = comm.isend(result, dest=0, tag=rank)

if rank == 0:
    results = np.zeros(size, dtype="i")
    requests = []
    
    for i in range(size):
        req = comm.irecv(source=i, tag=i)
        requests.append(req)
    
    for i in range(size):
        results[i] = requests[i].wait()
    
    print(f"Final results array: {results}")


