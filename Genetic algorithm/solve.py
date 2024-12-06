
                                                ##### PART1 #####
import random
# Create random population of chromosomes
def create_population_set(pop_size, N, T):
    population = []
    for p in range(pop_size):
        chromosome = []
        for i in range(N):
            timeslot = [0] * T
            timeslot[random.randint(0, T - 1)] = 1  
            chromosome.extend(timeslot)
        population.append(chromosome)
    return population
    


#calculate fitness for each chromosome
# def calculate_fitness(chromosome, N, T):
#     penalty_overlap = 0
#     penalty_consistency = 0
    
#     schedule = []
#     for i in range(N):
#         course_timeslots = chromosome[i * T:(i + 1) * T]
#         schedule.append(course_timeslots)
    
#     # Overlap penalty: Count overlapping courses in each timeslot
#     for t in range(T):
#         courses_in_timeslot = 0
#         for i in range(N):
#             courses_in_timeslot += schedule[i][t]
#         penalty_overlap += abs(courses_in_timeslot - 1)
    
#     # Consistency penalty: Count courses that appear more than once or not at all
#     for i in range(N):
#         times_scheduled = sum(schedule[i])
#         penalty_consistency += abs(times_scheduled - 1)
    
#     fitness = -(penalty_overlap + penalty_consistency)
#     return fitness

def calculate_fitness(chromosome, N, T):
    # Calculate overlap penalty
    overlap_penalty = 0
    for t in range(T):
        timeslot = chromosome[t * N:(t + 1) * N]
        scheduled_courses = sum(timeslot)
        if scheduled_courses == 0:
            overlap_penalty += 1
        if scheduled_courses > 1:
            overlap_penalty += (scheduled_courses - 1)
    
    # Calculate consistency penalty
    consistency_penalty = 0
    for n in range(N):
        scheduled_times = sum(chromosome[n + t * N] for t in range(T))
        consistency_penalty += abs(scheduled_times - 1)
    
    # Total penalty
    total_penalty = overlap_penalty + consistency_penalty
    
    # Fitness is the negative of the total penalty
    fitness = -total_penalty
    
    return fitness

def select_parents(population, fitness_values):

    total_fitness = sum(fitness_values)
    selected_parents = []
    while len(selected_parents) < 2:
        pick = random.uniform(0, total_fitness)
        current = 0
        for chromosome, fitness in zip(population, fitness_values):
            current += fitness
            if current > pick:
                selected_parents.append(chromosome)
                break
    return selected_parents

def crossover(parent1, parent2):

    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
   
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit
    return chromosome



def genetic_algorithm(N, T,pop_size=50, generations=500, mutation_rate=0.01):
    # Step 1: Initialize population
    population = create_population_set(pop_size, N, T)
    
    for gen in range(generations):
        # Step 2: Calculate fitness for each chromosome

        fitness_values = []
        for ch in population:
            fitness = calculate_fitness(ch, N, T)
            fitness_values.append(fitness)
        
        # Check for for the best case
        if max(fitness_values) == 0:
            break
        
        # Step 3: Selection and reproduction
        new_population = []
        for i in range(pop_size // 2):

            parent1, parent2 = select_parents(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        
        population = new_population
    
    # Return the best solution
    best_index = fitness_values.index(max(fitness_values))
    best_schedule = population[best_index]
    best_fitness = fitness_values[best_index]
    return best_schedule, best_fitness
# Number of courses
N = int(input("Enter the number of courses: "))

# Number of timeslots
T = int(input("Enter the number of timeslots: "))


best_schedule, best_fitness = genetic_algorithm(N, T)
output_schedule = ''.join(map(str, best_schedule))
print("Best schedule:", output_schedule)
print("Best fitness:", best_fitness)

                                                
print("PART1 COMPLETED")                                             
                                                
                                                ##### PART2 ######

def two_point_crossover(parent1, parent2):
    length = len(parent1)
    # Ensure the second point is always after the first point
    point1 = random.randint(0, length - 2)
    point2 = random.randint(point1 + 1, length - 1)

    # Create children by swapping segments between the two points
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2

# Example parents
parent1 = [0, 0, 0, 1, 1, 1, 0, 0, 0]
parent2 = [1, 1, 1, 0, 0, 0, 1, 1, 1]

# Perform two-point crossover
child1, child2 = two_point_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
