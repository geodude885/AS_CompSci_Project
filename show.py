import funcs

def showCreature(creature, x, y):
    if creature != False:
        noStroke()
        fill(funcs.mapBetween(creature.str, 0, 1, 0, 255), 0, 0)
        polygon(x, y, funcs.mapBetween(creature.sze, 0, 1, 0, 30), funcs.mapBetween(1/(creature.str/creature.sze), 0, 1, 0, 40))
        stroke(200)
    else:
        stroke(50)
        line(x-40, y-40, x+40, y+40)
        line(x+40, y-40, x-40, y +40)
    
def drawGrid(x ,y ,noCols ,noRows ,scl, colour, grdFill = None):
    stroke(colour)
    if grdFill:
        fill(grdFill)
        rect(x, y , (noRows * scl), (noCols * scl))
        
    for row in range(0, noRows + 1):
        line(x, y + row*scl, x + noCols*scl, y + row*scl)
        
    for col in range(0, noCols + 1):
        line(x + col * scl, y, x + col*scl, y + noRows * scl)
        
def drawCreatureGrid(generation):
    xPos, yPos = 60, height-780
    creatureNum = 0
    for yNum in range(len(generation)/10):
        for xNum in range(10):
            showCreature(generation[creatureNum], xPos, yPos)
            creatureNum += 1
            xPos += 80
        xPos = 60
        yPos += 80
        
def creatureInfo(creature):
    fill(150)
    if mouseY < height/2:
        rect(mouseX,mouseY, 120, 80)
    else:
        rect(mouseX, mouseY, 120, -80)
    
        
def polygon(x, y, radius, nPoints):
    angle = TWO_PI / nPoints
    beginShape()
    for p in range(int(nPoints)):
        p = p * angle
        dx = x + cos(p) * radius
        dy = y + sin(p) * radius
        vertex(dx, dy)
    endShape(CLOSE)