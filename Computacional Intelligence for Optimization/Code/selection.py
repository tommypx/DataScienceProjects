from random import uniform, sample
from operator import attrgetter
import numpy as np


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "min":
        # Sum total fitness
        total_fitness = sum([(1/i.fitness) for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += (1/individual.fitness)
            if position > spin:
                return individual

    elif population.optim == "max":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min).")



def tournament(population, size=50):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = sample(population.individuals, size)
    # Check if the problem is max or min
    if population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))

    elif population.optim == "max":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min).")

# Falta escrever o ranking

def ranking(population, size = 10):
    """ Ranking selection Implementation

    Args:
        population (Population): The population we want to select from.
        size(int): size of the population

    Returns:
        Individual: selected individual.
    """
    if population.optim == "min":
        # sorting the fitnesses
        sorted_fitnesses = [i.fitness for i in population].sort(reverse = True)
        # Total fitness for the ranking algorithm
        total_fitness = (size + 1) * size / 2


        incrementer = (total_fitness / size) / total_fitness
        ranking_scores = []

        while incrementer <= 1:
            ranking_scores.append(incrementer)
            incrementer += (total_fitness / size) / total_fitness

        ranking_scores = np.round(ranking_scores, 2).tolist()


        spin = uniform(0, sum(ranking_scores))
        position = 0
        # Find individual in the position of the spin
        for index, rank in enumerate(ranking_scores):
            position += rank
            if position > spin:
                return population[index]

    elif population.optim == "max":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min).")







