import time
import random
import multiprocessing
from multiprocessing import Semaphore

class ConnectionPool:
    def __init__(self, size):
        self.pool = [f"Connection-{i}" for i in range(size)]  
        self.semaphore = Semaphore(size)
        self.lock = multiprocessing.Lock()

    def get_connection(self):
        self.semaphore.acquire()
        with self.lock:  
            return self.pool.pop()

    def release_connection(self, connection):
        with self.lock:
            self.pool.append(connection)
        self.semaphore.release()

def access_database(pool, process_id):
    print(f"Process {process_id} is waiting for a connection...")
    connection = pool.get_connection()
    print(f"Process {process_id} acquired {connection}")
    time.sleep(random.uniform(1, 3))  
    print(f"Process {process_id} releasing {connection}")
    pool.release_connection(connection)