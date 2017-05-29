__author__ = 'George'

import random, genetic_creature
overallCreatureNum = 0

def genIteration(generation):

    global overallCreatureNum
    closest = 0

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

        poweredRandom = random.random() ** 20

        while closest == len(generation)-1:
            closest = min(range(len(chanceList)), key=lambda i: abs(chanceList[i]- poweredRandom))

        chanceList.remove(chanceList[closest])
        generation.remove(generation[closest])

    for parentNum in range(0, len(generation)-1):   # repopulates generation with creatures based on survivors from previous generation
        generation.append(genetic_creature.Creature(overallCreatureNum, generation[parentNum]))
        overallCreatureNum += 1

    generation = qsort(generation)


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

def main():
    validInput = False
    y = ""

    while validInput != True:
        try:
            genLen = int(input("Input creatures per generation"))
            validInput = True
        except:
            print("One or more inputs were invalid")


    generation = [genetic_creature.Creature(i) for i in range(genLen)] #creates initial parent generation for next to evolve from
    input()

    genNum = 0
    while True:
        for i in range(500):
            generation = genIteration(generation)

        print("GENERATION " + str(genNum) + " GENERATED:")
        genNum += 1

        for creature in generation:
            print(creature)
        if y != "":
            for creature in generation:
                print("parent num = " + str(creature.parent.num))
                print("parent fit = " + str(creature.parent.fitness))
                print("creature num = " + str(creature.num))
                print("fitness: " + str(creature.fitness))
                print("")
        if y == "inf":
            creature = generation[-1]
            print("num: " + str(creature.num))
            print("size: " + str(creature.size))
            print("per: " + str(creature.per))
            print("str: " + str(creature.str))
            print("int: " + str(creature.int))
            print("end: " + str(creature.end))
        y = input()


main()


#for i in range(len(creatureList/2)
#   creatureList.remove(int(map(random.random, 0, 1, 0, len(creatureList))))