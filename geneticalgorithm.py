from random import randint
import random

def individual(length, budget):
    # create a list of integer with a specific length
    min = (budget/length)-(round((budget/length)/2))
    max = (budget/length)+(round((budget/length)/2))
    return [randint(min,max) for x in range(length)]

def population(count, length, budget):
    # create specfic size of population which contains of list of integer
    return [individual(length, budget) for x in range(count)]

def fitness(individual,budget):
    # calculate the fitness score of each list of integer
    total = sum(individual)
    return abs(budget-total)

def grade(pop,budget):  
    # calculate the mean of the fitness score
    summed = [sum(i)-(budget) for i in pop]
    return (sum(summed)/len(pop))
    #return diff #(sum(tempList)/len(pop))

def evolve(pop,budget):
    retain=0.2
    random_select=0.05
    mutate=0.01
    
    # declare a nested list which contains list of integer
    # Select parents list with the best 20% fitness score
    graded = [(fitness(x,budget),x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    retain = int(len(graded)*retain)
    parents = graded[0:retain]
    
    #SELECTION
    for individual in graded[retain:]:
        # Random select element from the list with non parents element
        if random_select > random.random():
            parents.append(individual)
            
    #MUTATION
    for individual in parents:
        #Random mutate with a range of minimum and maximum of the selected list
        if mutate > random.random():
            pos_to_mutate = randint(0,len(individual)-1)
            individual[pos_to_mutate]= randint(min(individual),max(individual))
    
    #CROSS OVER
    #single point crossover
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0,parents_length-1)
        female = randint(0,parents_length-1)
        if male != female:
            male=parents[male]
            female=parents[female]
            #crossover point was selected at the middle of the list
            half = int(len(male)/2)
            child = male[:half]+female[half:]
            children.append(
                child)
            
    parents.extend(children)
    
    return parents
