__author__ = 'George'

import random


class Creature(object):
    def __init__(self, num, parent=None):
        try:

            self.size = parent.size - 0.000005 + (random.random() / 100000)
            self.per = parent.per - 0.000005 + (random.random() / 100000)
            self.str = parent.str - 0.000005 + (random.random() / 100000)
            self.int = parent.int - 0.000005 + (random.random() / 100000)
            self.end = parent.end - 0.000005 + (random.random() / 100000)

            #set limits for SIZE
            if self.size < 0:
                self.size = 10**-5
            if self.size > 1:
                self.size = 1.0

            #set limits for PERCEPTION
            if self.per > self.size - self.str - self.int:
                self.per = self.size - self.str - self.int
            if self.per < 0:
                self.per = 10**(-5)

            #set limits for STRENGTH
            if self.str < 0:
                self.str = 10**(-5)
            if self.str > self.size - self.per - self.int:
                self.str = self.size - self.per - self.int

            #set limits for INTELLIGENCE
            if self.int < 0:
                self.int = 10**(-5)
            if self.int > self.size - self.per - self.str:
                self.int = self.size - self.per - self.str

            #set limits for ENDURANCE
            if self.end < 0:
                self.end = 10**(-5)
            if self.end > 0.5/self.size:
                self.end = 0.5/self.size

        except AttributeError:
            self.parent = None
            self.size = random.uniform(10**(-7), 10**(-5))
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
        fitness = foodGathered * self.end

        return fitness

    def __str__(self):
        return "Creature " + str(self.num) + " Fitness: " + str(self.fitness) + "\n" + str(self.per)


    #size 0.0 - 1.0                             DONE
    #perception 0.0 - (size - str - int)        DONE
    #strength 0.0 - (size - per - int)          DONE
    #intelligence 0.0 - (size - per - str)      DONE
    #endurance 0.0 - (0.5/size)                 DONE

    #speed = strength/size
    #strength < (size * 3) / 4
    #strength < endurance
    #foodGathered = (speed + perception + intelligence)
    #endurance < 0.5/size

    #fitness = foodGathered * endurance


    #size 0.0 - 1.0
    #endurance: 0.0 - 1.0

