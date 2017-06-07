__author__ = 'George'

import random, funcs
MUTATIONRATE = 0.000001
DEATHRANDOMNESS = 3 #low is more random
overallCreatureNum = 0

def initialise(genLen):
    #creates initial parent generation for next to evolve from
    return  funcs.qsortGen([Creature(i) for i in range(genLen)])

class Creature(object):
    def __init__(self, num, parent=None):
        try:

            self.sze = parent.sze + random.uniform(-MUTATIONRATE , MUTATIONRATE)
            self.per = parent.per - (MUTATIONRATE * 0.5) + (random.random() / 1**MUTATIONRATE)
            self.stren = parent.stren - (MUTATIONRATE * 0.5) + (random.random() / 1**MUTATIONRATE)
            self.int = parent.int - (MUTATIONRATE * 0.5) + (random.random() / 1**MUTATIONRATE)
            self.end = parent.end - (MUTATIONRATE * 0.5) + (random.random() / 1**MUTATIONRATE)

            #set limits for sze
            if self.sze < MUTATIONRATE:
                self.sze = MUTATIONRATE
            if self.sze > 1:
                self.sze = 1.0

            #set limits for PERCEPTION
            if self.per > self.sze - self.stren - self.int:
                self.per = self.sze - self.stren - self.int
            if self.per < 0:
                self.per = MUTATIONRATE

            #set limits for STRENGTH
            if self.stren > self.sze - self.per - self.int:
                self.stren = self.sze - self.per - self.int
            if self.stren < 0:
                self.stren = MUTATIONRATE

            #set limits for INTELLIGENCE
            if self.int > self.sze - self.per - self.stren:
                self.int = self.sze - self.per - self.stren
            if self.int < 0:
                self.int = MUTATIONRATE

            #set limits for ENDURANCE
            if self.end < 0:
                self.end = MUTATIONRATE
            if self.end > 0.5/self.sze:
                self.end = 0.5/self.sze

        except AttributeError:
            global overallCreatureNum
            overallCreatureNum +=1
            self.parent = None
            self.sze = random.uniform(MUTATIONRATE, 0.5)
            self.per = random.uniform(0, self.sze/3)
            self.stren = random.uniform(0, self.sze/3)
            self.int = random.uniform(0, self.sze/3)
            self.end = random.uniform(0, self.sze)

            print("first creature " + str(num) + " made")

        self.num = num
        self.parent = parent

    @property
    def fitness(self):
        speed = self.stren/self.sze
        foodGathered = speed + self.per + self.int
        foodSurvival = foodGathered - self.sze
        survivalChance = self.end * self.int
        fitness = foodSurvival * survivalChance
        return fitness

    def __str__(self):
        return "Creature " + str(self.num) + "\nFitness: " + str(round(self.fitness, 4)) + "\nSize:" + str(round(self.sze,4))


    #sze 0.0 - 1.0                             DONE
    #perception 0.0 - (sze - str - int)        DONE
    #strength 0.0 - (sze - per - int)          DONE
    #intelligence 0.0 - (sze - per - str)      DONE
    #endurance 0.0 - (0.5/sze)                 DONE

    #speed = strength/sze
    #strength < (sze * 3) / 4
    #strength < endurance
    #foodGathered = (speed + perception + intelligence)
    #foodSurvival = foodGathered - sze
    #endurance < 0.5/sze

    #fitness = foodGathered * endurance


    #sze 0.0 - 1.0 
    #endurance: 0.0 - 1.0
    
def naturalSelection(generation):
    closest = 0

    #the next few lines lay the base for 'natural selection'
    #basically it makes a list of chances of survival those kills them with low values
    

    for numberKilled in range(int(len(generation)/2)): # kills half of the generation population based on fitness value

        toKill = int(funcs.mapBetween(1-(random.random() ** DEATHRANDOMNESS), 0, 1 ,0 , 100))
        while generation[toKill] == False:
            if toKill == -1:
                toKill = 99
            else:
                toKill -= 1
                
        generation[toKill] = False
        
    return generation
    
def reproduction(generation):
    global overallCreatureNum
    
    for parentNum in range(len(generation)):   # repopulates generation with creatures based on survivors from previous generation
        generation.append(Creature(overallCreatureNum, generation[parentNum]))
        overallCreatureNum += 1
        print("CreatureNum " + str(overallCreatureNum) + " made")

    
    
    generation = funcs.qsortGen(generation)


    return generation

def removeFalses(generation):
    while False in generation:
        for creature in generation:
            if creature == False:
                generation.remove(creature)
    return generation
    

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
        chance = funcs.mapBetween(creature.fitness, minFit, maxFit, 0, 1)
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

    generation = funcs.qsort(generation)


    return generation