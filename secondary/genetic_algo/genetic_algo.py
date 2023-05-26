import random
from answer import is_answer, get_score, get_mean_score, alphabet


def get_letter():
    return random.choice(alphabet)


def create_chromosome(size):
    # Create a chromosome as a string of the right size
    chromosome = ""
    for _ in range(size):
        chromosome += get_letter()
    return chromosome


def create_population(pop_size, chrom_size):
    # create the base population
    return [create_chromosome(chrom_size) for _ in range(pop_size)]


def selection(population):
    _Graded_retain_percent = 0.3  # percentage of retained best fitting individuals
    _Ungraded_retain_percent = 0.2  # percentage of retained remaining individuals (randomly selected)

    #  * Sort individuals by their fitting score
    pop_by_scores = sorted(population, key=lambda x: get_score(x), reverse=True)

    #  * Select the best individuals
    nb_best = int(len(pop_by_scores) * _Graded_retain_percent)
    selected_pop = pop_by_scores[:nb_best]

    #  * Randomly select other individuals
    nb_added = int(len(pop_by_scores) * _Ungraded_retain_percent)
    selected_pop += random.choice(pop_by_scores[nb_best: nb_best + nb_added])

    return selected_pop


def crossover(parent1, parent2):
    #  child = half_parent1 + half_parent2
    mid = len(parent1) // 2
    return parent1[:mid] + parent2[mid:]


def mutation(chrom):
    #  Random gene mutation : a character is replaced
    # if 1 < random.randrange(0, 1000) < 10 : # Mutation Probability : from 0.1% to 1%
    gene = random.choice(range(len(chrom)))
    mutated_chrom = chrom[:gene] + get_letter() + chrom[gene + 1:]
    # else:
    #    mutated_chrom = chrom[:]
    return mutated_chrom


def generation(population):
    # selection
    selected_pop = selection(population)

    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # implement the reproduction
    while len(children) < (len(population) - len(selected_pop)):
        ## crossover
        parent1 = random.choice(selected_pop)  # randomly selected
        parent2 = random.choice(selected_pop)  # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        child = crossover(parent1, parent2)

        ## mutation
        child = mutation(child)
        children.append(child)

    # return the new generation
    return selected_pop + children


def algorithm():
    chrom_size = int(input())
    population_size = int(input())
    chrom = ""

    # create the base population
    population = create_population(population_size, chrom_size)

    # while a solution has not been found :
    while True:
        ## create the next generation
        population = generation(population)

        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                break
        else:
            continue
        break

    # uncomment for more explainations and run genetic_algo_test
    #print(f"population={population}")
    #print(get_mean_score(population))

    # print the solution
    print(chrom)
