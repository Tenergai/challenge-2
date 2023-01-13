from deviceSpecification import getDevices
from utils import matrixToArray,arrayToMatrix
import numpy as np
import random
from objectiveFunction import objectiveFunction
from pyeasyga import pyeasyga
from generateMatrix import generateMatrix


devices = getDevices()
devicesHourly = generateMatrix(devices)

fitness_function = objectiveFunction

num_generations = 20

num_genes = 24*len(getDevices())
r_mut=0.01

# define a function to generate a random individual
def generate_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

# define a function to generate the initial population
def generate_population(devicesHourly):
    count=len(devicesHourly)
    length=len(devicesHourly[0])
    return [generate_individual(length) for _ in range(count)]


# define a function to perform genetic crossover (recombination)
def crossover(parent1, parent2):
    parent1=matrixToArray(parent1)
    parent2=matrixToArray(parent2)
    crossover_points = [24,48,72,96,120,144,168,192,216]
    child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]]+parent1[crossover_points[1]:crossover_points[2]] + parent2[crossover_points[2]:crossover_points[3]]+parent1[crossover_points[3]:crossover_points[4]] + parent2[crossover_points[4]:crossover_points[5]]+parent1[crossover_points[5]:crossover_points[6]] + parent2[crossover_points[6]:crossover_points[7]]+parent1[crossover_points[7]:crossover_points[8]] + parent2[crossover_points[8]:]
    child1=arrayToMatrix(child1)
    child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]]+parent2[crossover_points[1]:crossover_points[2]] + parent1[crossover_points[2]:crossover_points[3]]+parent2[crossover_points[3]:crossover_points[4]] + parent1[crossover_points[4]:crossover_points[5]]+parent2[crossover_points[5]:crossover_points[6]] + parent1[crossover_points[6]:crossover_points[7]]+parent2[crossover_points[7]:crossover_points[8]] + parent1[crossover_points[8]:]
    child2=arrayToMatrix(child2)
    return child1,child2

# define a function to perform mutation
def mutation(indiv, r_mut):
    for i in range(len(indiv)):
        # check for a mutation
        if np.random.rand() < r_mut:
            # flip the bit
            indiv[i] = 1 - indiv[i]
    return indiv

def mutation2(data):
    data2=[]
    for indiv in data:
        data2.append(mutation(indiv, r_mut))
        return data2
def ga():           
    ga_instance = pyeasyga.GeneticAlgorithm(
                        seed_data=devicesHourly,
                        population_size=num_genes, 
                        generations=num_generations, 
                        crossover_probability = 0.8, 
                        mutation_probability=0.1, 
                        elitism= True, 
                        maximise_fitness= True)
    ga_instance.create_individual=generate_population
    ga_instance.mutate_function=mutation2
    ga_instance.fitness_function=objectiveFunction
    ga_instance.crossover_function=crossover
    ga_instance.run()
    return ga_instance.best_individual()