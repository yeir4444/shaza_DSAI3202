

## Assignment Overview

This assignment involves implementing a genetic algorithm (GA) to solve the **fleet management problem**, where the goal is to optimize the routes for delivery vehicles in a city. The optimization aims to minimize the total distance traveled by the fleet while ensuring each delivery node in the city is visited exactly once by any vehicle.

### Key Concepts

1. **Genetic Algorithm (GA)**: A search heuristic inspired by the process of natural selection, used to solve optimization and search problems. It works by evolving a population of candidate solutions through iterations using selection, crossover, and mutation.

2. **Fleet Management Problem**: The task involves optimizing the routes for a fleet of delivery vehicles in a city, minimizing the total distance traveled while ensuring that each delivery location (node) is visited once. The problem is a variation of the **Traveling Salesman Problem (TSP)**.

### Assignment Breakdown

This assignment is divided into several parts:

1. **Part 1: Single Vehicle Optimization**
   - You start by optimizing the route for a **single vehicle** that needs to visit all nodes in the city.
   - The vehicle starts and ends at the depot (node 0).
   - The objective is to minimize the total distance traveled by the vehicle.
   - The city is represented as a graph, where each node corresponds to a delivery location, and the distances between the nodes are provided in a distance matrix (`city_distances.csv`).

2. **Part 2: Genetic Algorithm**
   - You implement a genetic algorithm to solve this optimization problem.
   - The genetic algorithm includes the following components:
     - **Population Initialization**: Create an initial population of routes (solutions).
     - **Fitness Evaluation**: Calculate the fitness of each solution (route) based on the total distance traveled. The fitness function is designed to minimize the distance.
     - **Selection**: Select individuals for crossover based on their fitness using **tournament selection**.
     - **Crossover**: Perform **order crossover (OX)** to combine the genetic material of two parent routes and create offspring.
     - **Mutation**: Apply **mutation** to introduce random changes in the offspring.
     - **Termination Condition**: The algorithm runs until a predefined number of generations or until an acceptable solution is found.
     - **output**:
     - Best Solution: [0, 14, 24, 31, 15, 5, 23, 2, 1, 19, 3, 10, 6, 20, 22, 29, 11, 9, 13, 4, 18, 7, 26, 21, 27, 25, 17, 28, 16, 12, 8, 30]
     - Total Distance: -1000000.0
     - Total time: 0.04037952423095703
3. **Part 3: Parallelization**
   - Once the sequential version of the genetic algorithm is working, you need to parallelize the algorithm to run over multiple machines or processes.
   - Parallelization is implemented using **MPI4PY**.
   - The goal is to distribute the population across multiple processes and parallelize the fitness calculation, selection, and other operations.
   - **output with city_distances_extended.csv**:
   - Generation 100 took 0.00 seconds.
   - Total time: 0.003268718719482422
   - Final Best Route: [0, 49, 5, 90, 87, 89, 81, 14, 7, 30, 39, 80, 62, 37, 94, 63, 25, 53, 16, 11, 77, 4, 29, 57, 15, 22, 42, 8, 20, 76, 74, 67, 2, 69, 85, 99, 56, 31, 9, 84, 93, 58, 13, 27, 59, 50, 1, 92, 21, 23, 18, 43, 10, 95, 72, 47, 82, 35, 28, 96, 19, 88, 64, 45, 70, 66, 26, 6, 68, 61, 51, 55, 73, 32, 40, 65, 75, 97, 12, 60, 46, 83, 41, 52, 71, 79, 54, 34, 17, 44, 98, 91, 36, 48, 86, 38, 33, 78, 24, 3]
   - **output with city_distances.csv**:
   - Generation 100 took 0.00 seconds.
   - Total time: 0.0022308826446533203
   - Final Best Route: [0, 21, 15, 13, 23, 2, 10, 6, 1, 20, 3, 30, 12, 11, 18, 22, 9, 4, 8, 26, 24, 17, 19, 16, 31, 7, 14, 27, 5, 25, 28, 29]
   - **output with MPI4PY on all machines**:
   - full discloser, me and my teammates couldn't get it to work for some reason and we have faced the same issue with lab6 execution. However, we mannaged to make it work on the MPI4PY lecture.

4. **Part 4: Enhancements**
   - After parallelizing the genetic algorithm, you need to improve it further by:
     - Ensure population size matches all_scores before selection.
           The IndexError happened because select_in_tournament assumed a larger population size than available scores.
     - Use np.minimum to prevent invalid indices in tournament selection.
           If num_tournaments * tournament_size > len(all_scores), it could result in invalid indices.
     - Broadcast the correct population size to all MPI processes.
           This ensures every process has the same updated population.
     - **output after enhancements with city_distances.csv**:
     - Generation 100 took 0.00 seconds.
     - Total time: 0.0013380050659179688
     - Final Best Route: [0, 21, 18, 6, 4, 25, 26, 13, 20, 3, 28, 17, 11, 16, 22, 31, 23, 29, 24, 5, 27, 19, 14, 30, 10, 12, 2, 8, 9, 15, 1, 7]
     - The efficiency of the enhanced implementation is 27.8% when using 6 processes.
     - The speedup achieved after enhancements is 1.67×.
     - **output after enhancements with city_distances_extended.csv**:
     - Generation 100 took 0.00 seconds.
     - Total time: 0.002903461456298828
     - Final Best Route: [0, 20, 28, 51, 26, 5, 85, 83, 66, 53, 76, 84, 88, 23, 21, 79, 38, 82, 17, 49, 40, 93, 87, 65, 86, 78, 96, 77, 47, 32, 97, 99, 56, 6, 27, 37, 33, 54, 30, 42, 60, 45, 90, 67, 7, 52, 61, 39, 46, 95, 55, 36, 29, 62, 43, 35, 11, 15, 44, 50, 68, 24, 4, 25, 75, 1, 81, 92, 74, 73, 3, 48, 8, 12, 57, 58, 41, 69, 13, 19, 14, 10, 31, 64, 94, 9, 80, 22, 34, 89, 98, 59, 18, 70, 16, 2, 91, 71, 72, 63]
     - The efficiency of the enhanced implementation is 18.8% when using 6 processes.
     - The speedup achieved after enhancements is  1.13x.
       
### **Adding More Cars to the Problem**  

    - To add more cars, each solution (chromosome) should represent multiple routes, one per vehicle. The fitness function must consider the total cost for all cars, ensuring balanced workload distribution. Crossover and mutation operators should allow swapping cities between vehicles while maintaining valid routes. Using **MPI**, the computation can be parallelized, assigning different cars to different processes for efficiency. Constraints like vehicle capacity and time limits should also be considered.
---

## Tools and Technologies

- **Python**: The primary programming language used to implement the genetic algorithm.
- **MPI4PY**: The Python library used to parallelize the algorithm over multiple processes or machines using the Message Passing Interface (MPI).
- **NumPy**: A fundamental library used for handling arrays and matrices, including the distance matrix for the city map.
- **CSV**: Used to load the city distance data from a file (`city_distances.csv`).
- **Genetic Algorithm Components**:
  - **Population**: A set of potential solutions represented as routes.
  - **Fitness Function**: A function to evaluate the quality of each route by calculating the total distance.
  - **Selection**: A method to select individuals for reproduction based on fitness.
  - **Crossover**: A method to combine two parent routes to generate offspring.
  - **Mutation**: A method to randomly alter a route to introduce diversity in the population.

---

## Detailed Algorithm Steps

### 1. **Population Initialization**
   - Initialize a population of routes where each route is a permutation of the delivery nodes (excluding the depot node).
   - The first node (depot) is fixed in all routes, and the remaining nodes are permuted randomly.

### 2. **Fitness Calculation**
   - The fitness function calculates the total distance traveled by a vehicle based on its route.
   - The distance matrix is used to calculate the distance between consecutive nodes in the route.
   - A large penalty is applied if an infeasible route is encountered (i.e., if two nodes are disconnected).

### 3. **Selection (Tournament Selection)**
   - In tournament selection, a subset of individuals (routes) is randomly selected, and the individual with the highest fitness is chosen as a parent for reproduction.
   - This process is repeated for multiple tournaments to select a pool of parents for crossover.

### 4. **Crossover (Order Crossover)**
   - Order Crossover (OX) combines two parent routes to produce two offspring.
   - A random segment from one parent is copied to the offspring, and the remaining positions are filled with the nodes from the other parent while preserving their relative order.

### 5. **Mutation**
   - Mutation randomly swaps two nodes in a route with a low probability (mutation rate). This introduces small changes to the solution to help explore different parts of the solution space.

### 6. **Termination Condition**
   - The algorithm continues for a predefined number of generations or until an optimal solution (or acceptable fitness) is reached.

---

## Parallelization with MPI4PY

### 1. **Distribute Population**
   - The population is divided into subpopulations, which are distributed across different MPI processes.
   - Each process calculates the fitness for its assigned individuals.

### 2. **Collect Results**
   - The fitness values for all individuals in the population are gathered and exchanged between processes using MPI communication.
   - The global best solution is determined by comparing the fitness values from all processes.

### 3. **Parallel Selection, Crossover, and Mutation**
   - Selection, crossover, and mutation operations can also be parallelized by applying them independently to subgroups of the population.
   - This reduces the overall execution time by performing these operations simultaneously on multiple processes.

### 4. **Performance Metrics**
   - After parallelizing the algorithm, you can compare the execution time before and after the enhancements to evaluate the performance improvement.

---

## Running the Algorithm

1. **Initialization**: The initial population is generated randomly using `generate_unique_population`.
2. **Fitness Evaluation**: Fitness values are calculated for each individual in the population.
3. **Selection**: Individuals are selected for reproduction based on their fitness.
4. **Crossover and Mutation**: New offspring are created using crossover and mutation operations.
5. **Termination**: The algorithm stops after a predefined number of generations or when an acceptable solution is found.

---

## Enhancements and Improvements

- **Parallelization**: By distributing the population and fitness evaluations across multiple processes, the algorithm can handle larger populations and reduce computation time.
- **Scaling**: As the city size increases (e.g., from 20 nodes to 100 nodes), the parallelized algorithm becomes essential to maintain reasonable computation times.

---

## Challenges

- **Infeasible Routes**: Handling disconnected nodes (routes that cannot be traveled directly between two nodes) requires proper penalty handling in the fitness function.
- **Parallelization**: Efficiently distributing tasks and handling communication between processes is challenging, but crucial for improving performance on large-scale problems.

---

## Future Improvements

- **Multiple Cars**: The algorithm can be extended to handle multiple delivery vehicles. This would involve assigning routes to multiple vehicles and ensuring each node is visited exactly once by one vehicle.
- **Dynamic Population Adjustment**: The algorithm can be enhanced by dynamically adjusting the population size or mutation rates based on the progress of the solution.
- **Hybrid Algorithms**: Combining genetic algorithms with other optimization techniques like simulated annealing or local search could further improve performance.

---

## Conclusion

This assignment demonstrates the application of genetic algorithms to solve a real-world optimization problem—route optimization for a fleet of delivery vehicles. By parallelizing the algorithm using MPI4PY, we can significantly reduce the computation time and scale the algorithm to handle more complex problems with larger cities and fleets. The enhancements and improvements implemented throughout the assignment contribute to better performance and solution quality.

