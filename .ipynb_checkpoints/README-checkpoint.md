

# DSAI 3202 – Parallel and Distributed Computing
## Lab 6: Distributed Computing Using mpi4py

### 1. Objectives:
The primary objective of this lab is to develop Python programs that take advantage of multiple machines to run parallel computations using the **mpi4py** library. This lab consists of exercises that involve parallel processing of tasks such as calculating squares of numbers and simulating virus spread in a population.

### 2. Tools and Concepts:
- **Python**: The programming language used to develop the parallel programs.
- **mpi4py**: Python bindings for MPI (Message Passing Interface), which allows parallel computation and communication between different machines.
- **pandas**: A library to handle and manipulate large datasets (optional, based on usage).

### 3. Exercises:

#### 3.a. Square Program
**Task**: Create a function to compute the square of a series of integers from 1 to `n`.

- **Parallelization**: The program must be parallelized using **mpi4py** to distribute the calculation of squares across multiple processes running on different machines.
- **Program File**: The provided script must be saved as `calculate_squares.py`.

##### Steps:
1. **Initialize the MPI Environment**:
   - Import the `mpi4py` library.
   - Initialize the communicator using `MPI.COMM_WORLD`.
   - Get the rank (ID) and size (number of processes) of the current process.

2. **Distribute Tasks**:
   - Each process will compute squares for a range of numbers. This involves splitting the range from 1 to `n` among the available processes.

3. **Collect Results**:
   - The root process (rank 0) gathers the results from all other processes.
   - The final output should include:
     - The size of the array of squares.
     - The last square in the array.
     - Time taken to compute the squares.

4. **Environment Setup**:
   - Ensure that **mpi4py** is installed on all machines that will run the program.
   - Copy the SSH ID from the main machine to the others to enable communication.
   - Use **SSH** to access each machine.

5. **Distribute the Program**:
   - Copy the `calculate_squares.py` file to each machine in the same directory or use a shared file system.
   - Create a host file (`machines.txt`) that lists the IP addresses of all machines involved.

6. **Execute the Program**:
   - Run the program across multiple machines by using the following command:
     ```bash
     mpirun -np [num_processes] --hostfile machines.txt python calculate_squares.py
     ```

7. **Modify for Large Numbers**:
   - Modify the program to compute squares up to \(10^8\) and assess its performance.

#### 3.b. Bonus Task:
- **Objective**: Compute the highest square possible within 300 seconds. The group that computes the highest square will be awarded a 5% bonus in the second assignment. Ensure that the program does not lose other results.

#### 4. Building an MPI Program for Virus Spread Simulation

**Task**: Simulate the spread of a virus in a population using MPI for distributed computation.

##### Steps:

1. **Step 1: Initialize the MPI Environment**:
   - Import the necessary libraries.
   - Initialize the MPI communicator using `MPI.COMM_WORLD`.
   - Get the rank and size of the current process using `comm.Get_rank()` and `comm.Get_size()`.

2. **Step 2: Define Parameters**:
   - Define parameters like the population size, virus spread chance, and vaccination rate. Example:
     ```python
     population_size = 100
     spread_chance = 0.3
     vaccination_rate = np.random.uniform(0.1, 0.5)
     ```

3. **Step 3: Initialize the Population**:
   - Initialize an array representing the population, where each element is 0 (uninfected).
   - Randomly infect a small percentage of individuals at the start:
     ```python
     if rank == 0:
         infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
         population[infected_indices] = 1
     ```

4. **Step 4: Implement Virus Spread Function**:
   - Create a function `spread_virus()` to simulate virus spread. This function will update the population based on infection rules and the spread chance.
     ```python
     def spread_virus(population):
         new_population = population.copy()
         # Implement virus spread logic
         return new_population
     ```

5. **Step 5: Simulate Virus Spread**:
   - For a set number of time steps (e.g., 10), simulate the virus spread:
     ```python
     for _ in range(10):
         population = spread_virus(population)
         if rank != 0:
             comm.send(population, dest=0)
         else:
             for i in range(1, size):
                 received_data = comm.recv(source=i)
                 population += received_data
     ```

6. **Step 6: Calculate Infection Rate**:
   - Calculate the infection rate based on the final infected population count and print the results:
     ```python
     total_infected = np.sum(population)
     infection_rate = total_infected / population_size
     print(f"Process {rank} Infection Rate: {infection_rate}")
     ```

7. **Step 7: Run and Experiment**:
   - Run the program on multiple processors and observe the different infection rates based on random vaccination rates assigned to each process.
   - Experiment with changing parameters such as the virus spread chance and vaccination rates to see how they affect the dynamics of the virus spread.

### 5. Conclusion:
This lab introduces the concept of parallel computing using **mpi4py**. The exercises are designed to provide hands-on experience in:
- Running distributed programs on multiple machines.
- Distributing tasks and collecting results across processes.
- Simulating real-world problems (such as virus spread) using parallel computation.

Through these exercises, students learn how to scale up computation tasks, optimize performance, and work with MPI for distributed computing.

### 6. Dependencies:
- **mpi4py**: Install using the following command:
  ```bash
  pip install mpi4py
  ```

- **NumPy**: Required for numerical operations, install using:
  ```bash
  pip install numpy
  ```

- **Pandas** (optional for some tasks):
  ```bash
  pip install pandas
  ```

