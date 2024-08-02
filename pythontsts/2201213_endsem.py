import numpy as np
import random
import time
import math

BOARD_SIZE = 8
print("Enter the temperature range")
TEMPERATURE_RANGE = (int(input()),int(input()))
print("Enter the cooling rate range")
COOLING_RATE_RANGE = (float(input()),float(input()))


def create_individual():
    return np.random.permutation(BOARD_SIZE)


def evaluate_board(board):
    n_attacking = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                n_attacking += 1
    return n_attacking


def crossover(parent1, parent2):
    cp = sorted(random.sample(range(1, BOARD_SIZE), 2))

    child1 = np.concatenate((parent1[:cp[0]], parent2[cp[0]:cp[1]],parent1[cp[1]:]))
    child2 = np.concatenate((parent2[:cp[0]], parent1[cp[0]:cp[1]],parent2[cp[1]:]))

    return child1, child2


def mutate(board, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(BOARD_SIZE), 2)
        board[idx1], board[idx2] = board[idx2], board[idx1]


def simulated_annealing(initial_board, initial_temperature, cooling_rate, max_iterations=500):
    current_board = initial_board
    current_energy = evaluate_board(current_board)

    best_board = current_board
    best_energy = current_energy

    temperature = initial_temperature

    for _ in range(max_iterations):
        new_board = current_board.copy()
        mutate(new_board, 1.0)

        new_energy = evaluate_board(new_board)

        if new_energy < current_energy or random.random() < math.exp((current_energy - new_energy) / temperature):
            current_board = new_board
            current_energy = new_energy

            if current_energy < best_energy:
                best_board = current_board
                best_energy = current_energy

        temperature *= cooling_rate

    return best_board, best_energy


def genetic_algorithm(population_size, mutation_rate, num_generations):
    population = [create_individual() for _ in range(population_size)]

    for generation in range(num_generations):
        fitness = [evaluate_board(board) for board in population]

        sorted_indices = np.argsort(fitness)
        parents = [population[i] for i in sorted_indices[:population_size // 2]]

        offspring = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            offspring.extend([child1, child2])

        for board in offspring:
            mutate(board, mutation_rate)

        population = offspring

    best_board = min(population, key=evaluate_board)
    best_energy = evaluate_board(best_board)

    return best_board, best_energy


population_size = int(input("Enter the population size:"))
mutation_rate = float(input("Enter the mutation rate:"))
num_generations = 500

initial_temperature = random.uniform(*TEMPERATURE_RANGE)
cooling_rate = random.uniform(*COOLING_RATE_RANGE)
initial_board = create_individual()

start_time = time.time()
best_board_sa, best_energy_sa = simulated_annealing(initial_board, initial_temperature, cooling_rate)
end_time = time.time()
sa_computational_time = end_time - start_time

start_time = time.time()
best_board_ga, best_energy_ga = genetic_algorithm(population_size, mutation_rate, num_generations)
end_time = time.time()
ga_computational_time = end_time - start_time

print("Simulated Annealing:")
print("Best board:", best_board_sa)
print("Attacking pairs:", best_energy_sa)
print("Computational time:", sa_computational_time, "seconds")

print("\nGenetic Algorithm:")
print("Best board:", best_board_ga)
print("Attacking pairs:", best_energy_ga)
print("Computational time:", ga_computational_time, "seconds")
