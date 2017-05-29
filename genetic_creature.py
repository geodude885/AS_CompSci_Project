__author__ = 'George'

import random
mutationRate = 0.000001


class Creature(object):
    def __init__(self, num, parent=None):
        try:

            self.size = parent.size + random.uniform(-mutationRate , mutationRate)
            self.per = parent.per - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.str = parent.str - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.int = parent.int - (mutationRate * 0.5) + (random.random() / 1**mutationRate)
            self.end = parent.end - (mutationRate * 0.5) + (random.random() / 1**mutationRate)

            #set limits for SIZE
            if self.size < mutationRate:
                self.size = mutationRate
            if self.size > 1:
                self.size = 1.0

            #set limits for PERCEPTION
            if self.per > self.size - self.str - self.int:
                self.per = self.size - self.str - self.int
            if self.per < 0:
                self.per = mutationRate

            #set limits for STRENGTH
            if self.str > self.size - self.per - self.int:
                self.str = self.size - self.per - self.int
            if self.str < 0:
                self.str = mutationRate

            #set limits for INTELLIGENCE
            if self.int > self.size - self.per - self.str:
                self.int = self.size - self.per - self.str
            if self.int < 0:
                self.int = mutationRate

            #set limits for ENDURANCE
            if self.end < 0:
                self.end = mutationRate
            if self.end > 0.5/self.size:
                self.end = 0.5/self.size

        except AttributeError:
            self.parent = None
            self.size = random.uniform(1, mutationRate)
            self.per = random.uniform(0, self.size/3)
            self.str = random.uniform(0, self.size/3)
            self.int = random.uniform(0, self.size/3)
            self.end = random.uniform(0, self.size)

            print("first creature " + str(num) + " made")

        self.num = num
        self.parent = parent

    @property
    def fitness(self):

        speed = self.str/self.size
        foodGathered = speed + self.per + self.int
        foodSurvival = foodGathered - self.size

        survivalChance = self.end * self.int


        fitness = foodSurvival * survivalChance

        return fitness

    def __str__(self):
        return "Creature " + str(self.num) + " Fitness: " + str(self.fitness) + "\n" + str(self.size)


    #size 0.0 - 1.0                             DONE
    #perception 0.0 - (size - str - int)        DONE
    #strength 0.0 - (size - per - int)          DONE
    #intelligence 0.0 - (size - per - str)      DONE
    #endurance 0.0 - (0.5/size)                 DONE

    #speed = strength/size
    #strength < (size * 3) / 4
    #strength < endurance
    #foodGathered = (speed + perception + intelligence)
    #foodSurvival = foodGathered - size
    #endurance < 0.5/size

    #fitness = foodGathered * endurance


    #size 0.0 - 1.0
    #endurance: 0.0 - 1.0

