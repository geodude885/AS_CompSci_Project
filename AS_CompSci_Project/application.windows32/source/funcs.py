
#Quicksorts the generation based upon fitness values
def qsortGen(list):
    
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsortGen([x for x in list[1:len(list)] if x.fitness < pivot.fitness])
        greater = qsortGen([x for x in list[1:len(list)] if x.fitness >= pivot.fitness])
        return lesser + [pivot] + greater

#Maps a value from one range to another range
def mapBetween(value, dataMin, dataMax, newMin, newMax):
    return (newMax - newMin) / (dataMax - dataMin) * (value - dataMax) + newMax
