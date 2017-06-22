__author__ = 'George'

import random, funcs

DEATHRANDOMNESS = 10 #low is more random, 3 is good
MAXSTARTSIZE = 0.1
MUTATIONMAX = 0.9
MUTATIONRATE = 19 #has to be odd
MINVAL = 0.00001
TYPEMUTECHANCE = 0.01

overallCreatureNum = 0

def initialise(genLen):
    #creates initial parent generation for next to evolve from
    generation = funcs.qsortGen([Creature(i) for i in range(genLen)])
    generation.reverse()
    return generation

class Creature(object):
    def __init__(self, num, parent=None):
        try:
            self.sze = -1
            self.per = -1
            self.stren = -1
            self.int = -1
            self.end = -1
            
            while self.fitness <= 0:
                self.sze = parent.sze + random.uniform(-MUTATIONMAX , MUTATIONMAX) ** MUTATIONRATE
                self.per = parent.per + random.uniform(-MUTATIONMAX , MUTATIONMAX) ** MUTATIONRATE
                self.stren = parent.stren + random.uniform(-MUTATIONMAX , MUTATIONMAX) ** MUTATIONRATE
                self.int = parent.int + random.uniform(-MUTATIONMAX , MUTATIONMAX) ** MUTATIONRATE
                self.end = parent.end + random.uniform(-MUTATIONMAX , MUTATIONMAX) ** MUTATIONRATE
    
                #set limits for sze
                if self.sze > 1:
                    self.sze = 1.0
                if self.sze < MINVAL:
                    self.sze = MINVAL
    
                #set limits for PERCEPTION
                if self.per > self.sze :
                    self.per = self.sze 
                if self.per < MINVAL:
                    self.per = MINVAL
    
                #set limits for INTELLIGENCE
                if self.int > self.sze :
                    self.int = self.sze 
                if self.int < MINVAL:
                    self.int = MINVAL
                
                #set limits for STRENGTH
                if self.stren > self.sze :
                    self.stren = self.sze 
                if self.stren < MINVAL:
                    self.stren = MINVAL
    
    
                #set limits for ENDURANCE
                if self.end > self.sze:
                    self.end = self.sze
                if self.end < MINVAL:
                    self.end = MINVAL
                    
                self.pnum = parent.num
                if random.random() < TYPEMUTECHANCE:
                    self.type *= random.randint(0, 10)
                else:    
                    self.type = parent.type

    
        except AttributeError:
            
            global overallCreatureNum
            overallCreatureNum +=1
            self.parent = None
            self.pnum = "No parent"
            self.type = overallCreatureNum
            
            while self.fitness <= 0:
                self.sze = random.uniform(MINVAL, MAXSTARTSIZE)
                self.per = random.uniform(MINVAL, self.sze)
                self.stren = random.uniform(MINVAL, self.sze)
                self.int = random.uniform(MINVAL, self.sze)
                self.end = random.uniform(0.5, self.sze)

        self.num = num
        self.parent = parent

    @property
    def fitness(self):
        
                speed = self.stren/self.sze
                foodGathered = speed + self.per + self.int
                foodSurvival = foodGathered - (self.sze/2)
                survivalChance = self.end * self.int
                fitness = foodSurvival * survivalChance
                #if self.stren + self.per + self.end > self.sze:
                #    fitness *= 0.1
                #if self.int > foodGathered/2:
                #    fitness /= 2
                return fitness
        

    def __str__(self):
        return ("Creature " + str(self.num) +
        "\nFitness: " + str(round(self.fitness, 4)) +
        "\nSize:" + str(round(self.sze,4)) + 
        "\nPerception:" + str(round(self.per,4)) +
        "\nStrength:" + str(round(self.stren,4)) +
        "\nIntelligence:" + str(round(self.int,4)) +
        "\nEndurance:" + str(round(self.end,4)) + 
        "\nParent: " + str(self.pnum))


    #sze 0.0 - 1.0                             DONE
    #perception 0.0 - 1                        DONE
    #strength 0.0 - 1                          DONE
    #intelligence 0.0 - 1                      DONE
    #endurance 0.0 - 1                         DONE

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

        toKill = int(funcs.mapBetween(1-(random.random() ** DEATHRANDOMNESS), 0, 1 ,1 , len(generation)-1))
        while generation[toKill] == False:
            if toKill == -1:
                toKill = len(generation)-1
            else:
                toKill -= 1
                
        generation[toKill] = False
        
    return generation
    
def reproduction(generation):
    global overallCreatureNum
    
    for parentNum in range(len(generation)):   # repopulates generation with creatures based on survivors from previous generation
        generation.append(Creature(overallCreatureNum, generation[parentNum]))
        overallCreatureNum += 1

    generation = funcs.qsortGen(generation)
    generation.reverse()

    return generation

def removeFalses(generation):
    while False in generation:
        for creature in generation:
            if creature == False:
                generation.remove(creature)
    return generation
    

def genIteration(generation):
    return reproduction(removeFalses(naturalSelection(generation)))