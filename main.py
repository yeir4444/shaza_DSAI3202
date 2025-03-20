import numpy as np
import pandas as pd
from mpi4py import MPI
from src.genetic_algorithms_functions import *
import time

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Parameters
num_generations = 100
population_size = 100
mutation_rate = 0.01
tournament_size = 3
num_tournaments = max(1, population_size // tournament_size)  # Ensure at least 1 tournament
distance_matrix = pd.read_csv('data/city_distances_extended.csv').to_numpy()

# Main GA loop
def genetic_algorithm():
    num_nodes = len(distance_matrix)
    population = generate_unique_population(population_size, num_nodes)

    # Distribute population across processes
    local_population = np.array_split(population, size)[rank]

    for generation in range(num_generations):
        start_time = time.time()

        # Compute local fitness scores
        local_scores = np.array([calculate_fitness(route, distance_matrix) for route in local_population])

        # Gather scores at root process
        all_scores = comm.gather(local_scores, root=0)

        if rank == 0:
            all_scores = np.concatenate(all_scores)

            # Ensure population and scores sizes match
            population = population[:len(all_scores)]  # Trim if necessary

            # Validate tournament selection
            max_valid_index = len(all_scores) - 1
            selected_parents = select_in_tournament(
                population, 
                all_scores, 
                min(num_tournaments, len(all_scores) // tournament_size), 
                min(tournament_size, len(all_scores))
            )

            # Generate offspring
            offspring = []
            for i in range(0, len(selected_parents), 2):
                parent1 = selected_parents[i]
                parent2 = selected_parents[i + 1] if i + 1 < len(selected_parents) else selected_parents[0]
                child1 = order_crossover(parent1, parent2)
                child2 = order_crossover(parent1, parent2)
                offspring.extend([child1, child2])

            # Mutate offspring
            mutated_offspring = [mutate(individual, mutation_rate) for individual in offspring]

            # Update population
            population = mutated_offspring[:population_size]  # Ensure correct population size

            # Print best fitness
            best_index = np.argmax(all_scores)
            best_fitness = all_scores[best_index]
            print(f"Generation {generation + 1}: Best Fitness = {best_fitness:.2f}")

        # Broadcast updated population
        population = comm.bcast(population, root=0)

        if rank == 0:
            end_time = time.time()
            print(f"Generation {generation + 1} took {end_time - start_time:.2f} seconds.")

    # Final results
    if rank == 0:
        total_time = end_time - start_time
        best_index = np.argmax(all_scores)
        best_route = population[best_index]
        print("Total time:", total_time)
        print("Final Best Route:", best_route)

if __name__ == "__main__":
    genetic_algorithm()
