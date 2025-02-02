from src.functions import *
from src.sequential_task import *
from src.threads_task import *
from src.processes_task import *
import time
import random
import string

# task 2_a: sequential
print("task 2_a: sequential")
run_sequential()

# task 2_b: threading
print("task 2_b: threading")
run_threads()

# task 2_c: processes
print("task 2_c: processes")
run_processes()
