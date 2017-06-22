import funcs, math
def showCreature(creature, x, y, font):
    if creature != False:
        noStroke()
        
        R = funcs.mapBetween(creature.stren, 0, 1, 0, 200)
        G = funcs.mapBetween(creature.per, 0, 1, 0, 200)
        B = funcs.mapBetween(creature.int, 0, 1, 0, 200)
        
        fill(R,G,B)
        noSides = funcs.mapBetween(creature.end, 0, 1, 3, 13) 
        showSize = funcs.mapBetween(creature.sze, 0, 1, 1, 15)
        
        polygon(x, y, showSize, noSides, creature.type)
        
        stroke(200)
        fill(0)
        #textFont(font, 16)
        #text(str(creature.num), x-30, y-20)
        
    else:
        stroke(50)
        line(x-16, y-17, x+16, y+12)
        line(x+16, y-17, x-16, y +12)
    
def drawGrid(x ,y ,noCols ,noRows ,xscl, yscl, colour, grdFill = None):
    stroke(colour)
    if grdFill:
        fill(grdFill)
        rect(x, y , (noCols * xscl), (noRows * yscl))
        
    for row in range(0, noRows + 1):
        line(x, y + row*yscl, x + noCols*xscl, y + row*yscl)
        
    for col in range(0, noCols + 1):
        line(x + col * xscl, y, x + col*xscl, y + noRows * yscl)
        
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
    if mouseY < height/2: yoff = 0
    else: yoff = 150
    if mouseX > width/2: xoff = 180
    else: xoff = 0
    
    fill(150)
    textFont(font, 16)
    rect(mouseX- xoff, mouseY -yoff-20, 180, 180)
    fill(0)
    if creature:
        text(str(creature), mouseX + 10-xoff, mouseY - yoff)
    else: 
        text("Creature is dead", mouseX + 10-xoff, mouseY - yoff + 20)
        
def polygon(x, y, radius, nPoints, type): #variance is val 0-1
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