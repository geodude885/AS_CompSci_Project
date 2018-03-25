import funcs
import math

def showCreature(creature, x, y, font):
    if creature != False:
        noStroke()
        
        fill(map(noise(creature.type), 0, 1, 150, 255), map(
            noise(creature.type + 1), 0, 1, 150, 255), map(noise(creature.type + 2), 0, 1, 150, 255))
        rect(x - 17, y - 17, 34, 31)
        
        R = funcs.mapBetween(creature.stren, 0, 1, 0, 200)
        G = funcs.mapBetween(creature.per, 0, 1, 0, 200)
        B = funcs.mapBetween(creature.int, 0, 1, 0, 200)

        fill(R, G, B)
        noSides = funcs.mapBetween(creature.end, 0, 1, 3, 13)
        showSize = funcs.mapBetween(creature.sze, 0, 1, 1, 15)

        polygon(x, y, showSize, noSides, creature.type)

        stroke(200)
        fill(0)
        #textFont(font, 16)
        #text(str(creature.num), x-30, y-20)

    else:
        stroke(50)
        line(x - 16, y - 17, x + 16, y + 12)
        line(x + 16, y - 17, x - 16, y + 12)

def drawGrid(x, y, noCols, noRows, xscl, yscl, colour, grdFill=None):
    stroke(colour)
    strokeWeight(1)
    if grdFill:
        fill(grdFill)
        rect(x, y, (noCols * xscl), (noRows * yscl))

    for row in range(0, noRows + 1):
        line(x, y + row * yscl, x + noCols * xscl, y + row * yscl)

    for col in range(0, noCols + 1):
        line(x + col * xscl, y, x + col * xscl, y + noRows * yscl)

def drawCreatureGrid(generation, font, stx, sty):
    xPos, yPos = stx, sty
    creatureNum = 0
    for yNum in range(25):
        for xNum in range(40):
            showCreature(generation[creatureNum], xPos, yPos, font)
            creatureNum += 1
            xPos += 35
        xPos = stx
        yPos += 32

def creatureInfo(creature, font):
    if mouseY < height / 2:
        yoff = 0
    else:
        yoff = 150
    if mouseX > width / 2:
        xoff = 180
    else:
        xoff = 0

    fill(150)
    textFont(font, 16)
    rect(mouseX - xoff, mouseY - yoff - 20, 180, 180)
    fill(0)
    if creature:
        text(str(creature), mouseX + 10 - xoff, mouseY - yoff)
    else:
        text("Creature is dead", mouseX + 10 - xoff, mouseY - yoff + 20)

def polygon(x, y, radius, nPoints, type):  # variance is val 0-1
    angle = TWO_PI / nPoints

    beginShape()

    i = 0
    for p in range(int(nPoints)):
        p = p * angle
        dx = x + cos(p) * radius * noise(type + i)
        dy = y + sin(p) * radius * noise(type + i)
        i += 1000
        vertex(dx, dy)
    endShape(CLOSE)


class Slider(object):

    def __init__(self, x, y, l, font, name):
        self.x = x
        self.y = y
        self.l = l
        self.pos = int(l\2)
        self.font = font
        self.name = name

    def show(self):
        if mousePressed:
            if self.x < mouseX < self.x + self.l and self.y - 10 < mouseY < self.y + 10:
                self.pos = mouseX - self.x
        stroke(200)
        fill(200)
        textFont(self.font, 32)
        text(str(round(self.value, 2))[0:4], self.x + self.l + 20, self.y + 10)
        text(self.name, self.x, self.y - 20)
        strokeWeight(5)
        line(self.x, self.y, self.x + self.l, self.y)
        stroke(100)
        strokeWeight(3)
        line(self.x, self.y, self.x + self.l, self.y)

        stroke(200)
        strokeWeight(10)
        line(self.x + self.pos, self.y - 6, self.x + self.pos, self.y + 6)
        stroke(100)
        strokeWeight(7)
        line(self.x + self.pos, self.y - 6, self.x + self.pos, self.y + 6)
        

    @property
    def value(self):
        return float(self.pos) / self.l

def graphData(arr, x, y, w, h, font, maxVal, rval=0,):

    stroke(0)
    strokeWeight(1)
    line(x, y, x, y + h)
    line(x, y + h, x + w, y + h)
    fill(0)
    textFont(font, 16)
    text("0", x, y + h + 17)
    text(str(len(arr)), x + w - 16, y + h + 17)
    text(str(round(maxVal, 4)), x - 16, y - 4)

    if len(arr) != 0:
        xspacing = float(w) / float(len(arr))
    else:
        xspacing = w
    dx = xspacing

    stroke(rval, 0, 0)
    prevPoint = 0
    yMult = h / maxVal

    for plotPoint in arr:
        x1 = x + dx - xspacing
        x2 = x + dx
        y1 = y + h - (prevPoint * yMult)
        y2 = y + h - (plotPoint * yMult)

        line(x1, y1, x2, y2)

        prevPoint = plotPoint
        dx += xspacing

def showFitGraph(font, topFit, botFit, avgFit, generation, name):
    strokeWeight(1)
    rect(10, 10, 550, 280)
    fill(0)
    textFont(font, 24)
    text(name, 25, 35)
    maxVal = 0
    for creature in generation:
        if creature.fitness > maxVal:
            maxVal = creature.fitness
    graphData(topFit, 40, 70, 500, 200, font, maxVal)
    graphData(avgFit, 40, 70, 500, 200, font, maxVal, 255)
    graphData(botFit, 40, 70, 500, 200, font, maxVal)

def showTypeChart(x, y, sze, types, font):
    angle = 0
    tot = 0
    firstType, secondType, thirdType = 0, 0, 0
    firstTypeNo, secondTypeNo, thirdTypeNo = -1, -1, -1

    for n in [type[1] for type in types]:
        tot += n

    for type in types:
        if type[1] > thirdTypeNo:
            if type[1] > secondTypeNo:
                if type[1] > firstTypeNo:
                    firstType = type[0]
                    firstTypeNo, secondTypeNo, thirdTypeNo = type[
                        1], firstTypeNo, secondTypeNo
                else:
                    secondType = type[0]
                    secondTypeNo, thirdTypeNo = type[1], secondTypeNo
            else:
                thirdType = type[0]
                thirdTypeNo = type[1]

        fill(map(noise(type[0]), 0, 1, 0, 255), map(
            noise(type[0] + 1), 0, 1, 0, 255), map(noise(type[0] + 2), 0, 1, 0, 255))
        prevAngle = angle
        angle = angle + (((2 * PI) / tot) * type[1])
        arc(x, y, sze, sze, prevAngle, angle)
    fill(200)
    rect(x + 190, y - sze / 2 + 15, 280, 180)

    string = ("Dominant Types:\n\n" +
              "1st:    Type " + str(firstType) + "  at: " + str(float(firstTypeNo) / 10) + "%" +
              "\n\n2nd:    Type " + str(secondType) + "  at: " + str(float(secondTypeNo) / 10) + "%" +
              "\n\n3rd:    Type " + str(thirdType)) + "  at: " + str(float(thirdTypeNo) / 10) + "%"

    fill(map(noise(firstType), 0, 1, 0, 255), map(
        noise(firstType + 1), 0, 1, 0, 255), map(noise(firstType + 2), 0, 1, 0, 255))
    rect(x + 205, y - 83, 50, 20)
    fill(map(noise(secondType), 0, 1, 0, 255), map(
        noise(secondType + 1), 0, 1, 0, 255), map(noise(secondType + 2), 0, 1, 0, 255))
    rect(x + 205, y - 38, 50, 20)
    fill(map(noise(thirdType), 0, 1, 0, 255), map(
        noise(thirdType + 1), 0, 1, 0, 255), map(noise(thirdType + 2), 0, 1, 0, 255))
    rect(x + 205, y + 7, 50, 20)
    fill(0)
    textFont(font, 18)
    text(string, x + 210, y - sze / 2 + 40)