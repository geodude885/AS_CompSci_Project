__author__ = 'George'

import random, funcs
mutationRate = 0.000001


class Creature(object):
    def __init__(self, num, parent=None):
        try:

            self.sze = parent.sze + random.uniform(-mutationRate , mutationRate)
            self.per = parent.per - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.str = parent.str - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.int = parent.int - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.end = parent.end - (mutationRate * 0.5) + (random.random() / 1**mutationRate)

            #set limits for sze
            if self.sze < mutationRate:
                self.sze = mutationRate
            if self.sze > 1:
                self.sze = 1.0

            #set limits for PERCEPTION
            if self.per > self.sze - self.str - self.int:
                self.per = self.sze - self.str - self.int
            if self.per < 0:
                self.per = mutationRate

            #set limits for STRENGTH
            if self.str > self.sze - self.per - self.int:
                self.str = self.sze - self.per - self.int
            if self.str < 0:
                self.str = mutationRate

            #set limits for INTELLIGENCE
            if self.int > self.sze - self.per - self.str:
                self.int = self.sze - self.per - self.str
            if self.int < 0:
                self.int = mutationRate

            #set limits for ENDURANCE
            if self.end < 0:
                self.end = mutationRate
            if self.end > 0.5/self.sze:
                self.end = 0.5/self.sze

        except AttributeError:
            self.parent = None
            self.sze = random.uniform(1, mutationRate)
            self.per = random.uniform(0, self.sze/3)
            self.str = random.uniform(0, self.sze/3)
            self.int = random.uniform(0, self.sze/3)
            self.end = random.uniform(0, self.sze)

            print("first creature " + str(num) + " made")

        self.num = num
        self.parent = parent

    @property
    def fitness(self):
        speed = self.str/self.sze
        foodGathered = speed + self.per + self.int
        foodSurvival = foodGathered - self.sze
        survivalChance = self.end * self.int
        fitness = foodSurvival * survivalChance
        return fitness

    def __str__(self):
        return "Creature " + str(self.num) + " Fitness: " + str(self.fitness) + "\n" + str(self.sze)


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

    minFit = min([creature.fitness for creature in generation])
    maxFit = max([creature.fitness for creature in generation])

    if minFit == maxFit:
       maxFit += maxFit
    

    for numberKilled in range(int(len(generation)/2)): # kills half of the generation population based on fitness value

        toKill = int(funcs.mapBetween(1-(random.random() ** 22), 0, 1 ,0 , 99))
        while generation[toKill] == False:
            if toKill == 99:
                toKill = 0
            else:
                toKill += 1
                
        generation[toKill] = False
        
        #chanceList[closest] = 1
        #generation[closest] = False 
    

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