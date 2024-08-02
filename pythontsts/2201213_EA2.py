import numpy as np
import random
import time

NUM_QUESTIONS = 10
POP_SIZE = 15
CROSSOVER_PROB = 0.6
MUTATION_PROB = 0.5
MAX_GENS = 30

def init_pop(pop_size, num_questions):
    population = np.random.randint(2, size=(pop_size, num_questions))
    return population

def fitness(individual):
    return np.sum(individual)

def roulette_selection(population, fitness_values):
    probs = fitness_values / np.sum(fitness_values)
    selected_indices = np.random.choice(len(population), size=2, p=probs)
    return population[selected_indices[0]], population[selected_indices[1]]

def multi_crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, NUM_QUESTIONS), 3))
    child1 = np.concatenate((parent1[:crossover_points[0]], parent2[crossover_points[0]:crossover_points[1]], parent1[crossover_points[1]:crossover_points[2]],parent1[crossover_points[2]:]))
    child2 = np.concatenate((parent2[:crossover_points[0]], parent1[crossover_points[0]:crossover_points[1]], parent2[crossover_points[1]:crossover_points[2]],parent1[crossover_points[2]:]))
    return child1, child2

def bit_flip_mutation(individual):
    mutation_indices = np.random.choice(NUM_QUESTIONS, int(MUTATION_PROB * NUM_QUESTIONS), replace=False)
    mutated_individual = np.copy(individual)
    for idx in mutation_indices:
        mutated_individual[idx] = 1 - mutated_individual[idx]
    return mutated_individual

def genetic_algorithm():
    population = init_pop(POP_SIZE, NUM_QUESTIONS)
    print(population)
    best_solution = None
    best_fitness = -1

    for generation in range(MAX_GENS):
        fitness_vals = np.array([fitness(individual) for individual in population])

        selected_parents = [roulette_selection(population, fitness_vals) for _ in range(POP_SIZE // 2)]

        children = [multi_crossover(parent1, parent2) for parent1, parent2 in selected_parents]
        children = np.array(children).reshape(-1, NUM_QUESTIONS)

        for idx in range(len(children)):
            if np.random.rand() < MUTATION_PROB:
                children[idx] = bit_flip_mutation(children[idx])

        population = np.vstack((population, children))
        population = population[np.argsort([fitness(individual) for individual in population])[-POP_SIZE:]]

        current_best = population[np.argmax([fitness(individual) for individual in population])]
        current_best_fitness = fitness(current_best)
        if current_best_fitness > best_fitness:
            best_solution = current_best
            best_fitness = current_best_fitness

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    return best_solution, best_fitness

start_time = time.time()
best_solution, best_fitness = genetic_algorithm()
end_time = time.time()
print("\nBest Solution:", best_solution)
print("Best Fitness:", best_fitness)
print("Computational Time:", end_time - start_time, "seconds")
