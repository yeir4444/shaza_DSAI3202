## iv) Discuss Observations:
# • What happens if more processes try to access the pool than there are available connections?
    - Processes that exceed the available connections must wait until an existing connection is released.
    - The semaphore ensures that only a limited number of processes can proceed at a time, preventing overload.

# • How does the semaphore prevent race conditions and ensure safe access to the connections?
    - The semaphore controls access by allowing only a fixed number of processes to acquire connections.
    - The use of a lock (`multiprocessing.Lock()`) ensures that only one process modifies the connection pool at a time.
    - This prevents multiple processes from simultaneously taking or returning the same connection, avoiding inconsistencies.
