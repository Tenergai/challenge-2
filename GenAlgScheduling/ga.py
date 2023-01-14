from deviceSpecification import getDevices
from utils import matrixToArray,arrayToMatrix
import numpy as np
from objectiveFunction import objectiveFunction,c,r
from pyeasyga import pyeasyga
from generateMatrix import generateMatrix
from genMatrixWithRepair import generateAndRepair, validateChild

devices = getDevices()
devicesHourly, n, o , p=generateAndRepair(1, 100)
devicesHourly=devicesHourly[0]
fitness_function = objectiveFunction

num_generations = 20

num_genes = r*c
r_mut=0.01

# define a function to generate the initial population
def generate_population(d):
    m, n, o , p=generateAndRepair(4, 100)
    return m[0]

# define a function to perform genetic crossover (recombination)
def crossover(parent1, parent2):
    parent1=parent1[0]
    parent2=parent2[0]
    parent1=matrixToArray(parent1)
    parent2=matrixToArray(parent2)
    crossover_points = [24,48,72,96,120,144,168,192,216]
    child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]]+parent1[crossover_points[1]:crossover_points[2]] + parent2[crossover_points[2]:crossover_points[3]]+parent1[crossover_points[3]:crossover_points[4]] + parent2[crossover_points[4]:crossover_points[5]]+parent1[crossover_points[5]:crossover_points[6]] + parent2[crossover_points[6]:crossover_points[7]]+parent1[crossover_points[7]:crossover_points[8]] + parent2[crossover_points[8]:]
    child1=arrayToMatrix(child1)
    child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]]+parent2[crossover_points[1]:crossover_points[2]] + parent1[crossover_points[2]:crossover_points[3]]+parent2[crossover_points[3]:crossover_points[4]] + parent1[crossover_points[4]:crossover_points[5]]+parent2[crossover_points[5]:crossover_points[6]] + parent1[crossover_points[6]:crossover_points[7]]+parent2[crossover_points[7]:crossover_points[8]] + parent1[crossover_points[8]:]
    child2=arrayToMatrix(child2)
    r1=validateChild(child1)
    r2=validateChild(child2)
    child1=(child1,r1[1])
    child2=(child2,r2[1])
    if r1[0]==False:
        child1=generateAndRepair(1,100)
    if r2[0]==False:
        child2=generateAndRepair(1,100)
    return child1,child2 

# define a function to perform mutation
def mutation(indiv, r_mut):
    print('i',indiv)
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
                        mutation_probability=r_mut, 
                        elitism= True, 
                        maximise_fitness= True)
    ga_instance.create_individual=generate_population
    ga_instance.mutate_function=mutation2
    ga_instance.fitness_function=objectiveFunction
    ga_instance.crossover_function=crossover
    ga_instance.run()
    return ga_instance.best_individual()