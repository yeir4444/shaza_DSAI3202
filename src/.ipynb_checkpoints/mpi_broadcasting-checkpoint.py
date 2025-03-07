from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the IP address of the current machine (the VM)
ip_address = socket.gethostbyname(socket.gethostname())

if rank == 0:
    # Process 0 broadcasts a message to all processes
    data_to_send = "Hello from Process 0"
    comm.bcast(data_to_send, root=0)
    print("Process 0 broadcasted data")
else:
    # Other processes receive the broadcasted message correctly
    data_received = comm.bcast(None, root=0)  # All ranks must call bcast the same way
    print(f"Process {rank} received data: {data_received}")
    print(f"Process {rank} (IP: {ip_address}) received the broadcasted message.")
