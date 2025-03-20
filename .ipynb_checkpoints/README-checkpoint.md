# Square program run:

**Testing with 1000000 numbers**:
    Sequential: 0.0043 seconds
    Multiprocessing Pool (map): 0.0222 seconds
    Multiprocessing Pool (map): 0.0180 seconds
    Multiprocessing Pool (apply): 15.4584 seconds
    ProcessPoolExecutor: 11.7314 seconds
    Asynchronous ProcessPoolExecutor: 0.0604 seconds
    
**Testing with 10000000 numbers** :
    Sequential: 0.0399 seconds
    Multiprocessing Pool (map): 0.0902 seconds
    Multiprocessing Pool (map): 0.0938 seconds
    Multiprocessing Pool (apply): 169.7106 seconds
    ProcessPoolExecutor: 112.1719 seconds
    Asynchronous ProcessPoolExecutor: 0.3242 seconds

# Process Synchronization with Semaphores run:

    Process 0 is waiting for a connection...
    Process 0 acquired Connection-2
    Process 1 is waiting for a connection...
    Process 1 acquired Connection-2
    Process 2 is waiting for a connection...
    Process 2 acquired Connection-2
    Process 3 is waiting for a connection...
    Process 4 is waiting for a connection...
    Process 5 is waiting for a connection...
    Process 2 releasing Connection-2
    Process 3 acquired Connection-2
    Process 0 releasing Connection-2
    Process 4 acquired Connection-2
    Process 1 releasing Connection-2
    Process 5 acquired Connection-2
    Process 3 releasing Connection-2
    Process 5 releasing Connection-2
    Process 4 releasing Connection-2


# Discuss Observations:
## • What happens if more processes try to access the pool than there are available connections?
    - Processes that exceed the available connections must wait until an existing connection is released.
    - The semaphore ensures that only a limited number of processes can proceed at a time, preventing overload.

## • How does the semaphore prevent race conditions and ensure safe access to the connections?
    - The semaphore controls access by allowing only a fixed number of processes to acquire connections.
    - The use of a lock (`multiprocessing.Lock()`) ensures that only one process modifies the connection pool at a time.
    - This prevents multiple processes from simultaneously taking or returning the same connection, avoiding inconsistencies.
