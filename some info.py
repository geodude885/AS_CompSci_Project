__author__ = 'George'

import random
overallCreatureNum = 0


class Creature(object):
    def __init__(self, num, parent = None):
        try:
            self.fitness = parent.fitness - 0.005 + (random.random() / 100)
            if self.fitness < 0:
                self.fitness = 10**-10
            if self.fitness > 1:
                self.fitness = 1
        except:
            self.parent = None
            self.fitness = 10**(-10)
            print("first creature " + str(num) + " made")
        self.num = num


    @property
    def fittness(self):
        maxStats = self.size()

        pass

    def __str__(self):
        return "Creature " + str(self.num) + " Fitness: " + str(self.fitness)

    #size
    #perception
    #strength
    #intelligence
    #endurance

    #sum of attributes is equal to size

    #speed = strength/size
    #


def main():
    validInput = False
    while validInput != True:
        try:
            genLen = int(input("Input creatures per generation"))
            validInput = True
        except:
            print("One or more inputs were invalid")


    generation = [Creature(i) for i in range(genLen)] #creates initial parent generation for next to evolve from
    input()

    for i in range(4000):
        generation = genIteration(generation)
        for creature in generation:
            print(creature)
        input()


def genIteration(generation):

    global overallCreatureNum

                                    #the next few lines lay the base for 'natural selection'
                                    #basically it makes a list of chances of survival those kills them with low values

    minFit = min([creature.fitness for creature in generation])
    maxFit = max([creature.fitness for creature in generation])

    if minFit == maxFit:
       maxFit += maxFit

    chanceList = []
    for creature in generation:
        chance = mapBetween(creature.fitness, minFit, maxFit, 0, 1)
        chanceList.append(chance)



    for numberKilled in range(int(len(generation)/2)): # kills half of the generation population based on fitness value

        poweredRandom = random.random() ** 10
        closest = min(range(len(chanceList)), key=lambda i: abs(chanceList[i]- poweredRandom))

        chanceList.remove(chanceList[closest])
        generation.remove(generation[closest])

    for parentNum in range(len(generation)):   # repopulates generation with creatures based on survivors from previous generation
        generation.append(Creature(overallCreatureNum, generation[parentNum]))
        overallCreatureNum += 1

    generation = qsort(generation)

    print("GENERATION GENERATED:")


    return generation



def qsort(list):
    if list == []:
        return []
    else:
        pivot = list[0]

        lesser = qsort([x for x in list[1:len(list)] if x.fitness < pivot.fitness])

        greater = qsort([x for x in list[1:len(list)] if x.fitness >= pivot.fitness])

        return lesser + [pivot] + greater


def mapBetween(value, dataMin, dataMax, newMin, newMax):
    return (newMax - newMin) / (dataMax - dataMin) * (value - dataMax) + newMax


main()


#for i in range(len(creatureList/2)
#   creatureList.remove(int(map(random.random, 0, 1, 0, len(creatureList))))