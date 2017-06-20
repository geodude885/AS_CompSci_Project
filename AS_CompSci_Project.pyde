__author__ = 'George'
#screen = 2880 x 1800

import random, genetic_creature, show, funcs
genLen = 1000
generation = genetic_creature.initialise(genLen)
genCount = 0
creatScreen = True

def setup():
    fullScreen()
    background(21, 34, 56)
    
    global hoverButton
    hoverButton = Button(1350, 840, 70, 40, "Info", 5)
    
    global killButton
    killButton = Button(1240, 840, 70, 40, "Kill", 10)
    
    global reprButton
    reprButton = Button(1020, 840 ,180, 40, "Reproduce", 10)
    
    global iterButton
    iterButton = Button(1020, 760 ,180, 40, "Iteration", 10)
    
    
    global font
    font = loadFont("SansSerif-120.vlw")
    textFont(font, 32)
    updateScreen()

def draw():

    if 10 < mouseX < 1420 and 30 < mouseY < height or hoverButton.check == True:
        updateScreen()

    if killButton.check == True or reprButton.check == True: 
        cursor(HAND)    
    
    else: cursor(ARROW)
    

def updateScreen():
    clear()
    background(21, 34, 56)
    
    if creatScreen:
        show.drawGrid(20, 40, 40, 25, 35, 32, 200, 100)
        show.drawCreatureGrid(generation, font, 38, height-842)
        
        if 10 < mouseX < 1420 and 20 < mouseY < 840:
            xIndex = int((mouseX-20)/35)
            yIndex = int((mouseY-72)/32)
            creatureIndex = (40*(yIndex-1) + xIndex)
            show.creatureInfo(generation[creatureIndex], font)
        
    else:
        fill(200)
        textFont(font, 52)
        text("     EVOLUTION\nSIMULATOR V1", 1060, 60)
        text("GEN: " + str(genCount), 840, 186)
        
        
        if hoverButton.check == True:
            dispInfo()
            cursor(HAND)
        
            
        hoverButton.showButton()
        killButton.showButton()
        reprButton.showButton()
        iterButton.showButton()
        
def keyPressed():
    if key == TAB:
        global creatScreen
        creatScreen = not creatScreen
        updateScreen()
    if key in ("I", "i"):
        global generation, genCount
        generation = genetic_creature.genIteration(generation)
        genCount += 1
        updateScreen()

def mouseClicked():
    
    if hoverButton.check == True:
        updateScreen()
    
    if killButton.check == True:
        global generation
        generation = genetic_creature.naturalSelection(generation)
        updateScreen()

        
    if reprButton.check == True:
        global generation, genCount
        generation = genetic_creature.removeFalses(generation)
        generation = genetic_creature.reproduction(generation)
        genCount += 1
        updateScreen()
        
    if iterButton.check == True:
        global generation, genCount
        generation = genetic_creature.genIteration(generation)
        genCount += 1
        updateScreen()
        
    
class Button():
    def __init__(self, x, y, w, h, words = None, textOffset = None, colour = 210 ,tColour = 0,):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.colour, self.tColour = colour, tColour
        self.words, self.textOffset = words, textOffset
        
    def showButton(self):
        fill(self.colour)
        rect(self.x,self.y,self.w,self.h)
        fill(self.tColour)
        if self.words:
            textFont(font, 32)
            if not self.textOffset:
                self.textOffset = 0
            text(self.words, self.x + self.textOffset, self.y + 32)
        
    @property
    def check(self):
        if self.x < mouseX < self.x + self.w and self.y < mouseY < self.y + self.h:
            return True
        else: return False
        
def dispInfo():        
    fill(150)
    rect(1420,880, -820, -600)
    fill(0)
    textFont(font, 32)
    textLeading(15)
    text(
         """Info\n
This is placeholder text\n
which will eventually be replace by\n
text which describes how the evolution\n
algorithm works."""
         , 620, 320)


#run for initial generaion:

#generation = genIteration(generation)




#for i in range(len(creatureList/2)
#   creatureList.remove(int(map(random.random, 0, 1, 0, len(creatureList))))