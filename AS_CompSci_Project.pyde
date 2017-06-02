__author__ = 'George'
#screen = 2880 x 1800
import random, genetic_creature, show, funcs
genLen = 100
generation = [genetic_creature.Creature(i) for i in range(genLen)] #creates initial parent generation for next to evolve from
generation = funcs.qsort(generation)

def setup():
    fullScreen()
    background(21, 34, 56)
    
    global hoverButton
    hoverButton = Button(1350, 840, 70, 40)
    
    global killButton
    killButton = Button(1240,840, 70, 40, "Kill", 10)
    
    global font
    font = loadFont("SansSerif-120.vlw")
    textFont(font, 32)

def draw():
    clear()
    background(21, 34, 56)
    hoverButton.showButton()
    killButton.showButton()
    
    show.drawGrid(20, height-820, 10, 10, 80, 200, 100)
    show.drawCreatureGrid(generation)
    
    if hoverButton.check == True:
        dispInfo()
        cursor(HAND)
    elif killButton.check == True: 
        cursor(HAND)
    else: cursor(ARROW)
    

def mouseClicked():
    
    if hoverButton.check == True:
        rect(1420,880, -820, -600)
    
    if killButton.check == True:
        global generation
        generation = genetic_creature.naturalSelection(generation)
    
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
            if not self.textOffset:
                self.textOffset = 0
            text(self.words, self.x + self.textOffset, self.y + 32)
        
    @property
    def check(self):
        if self.x < mouseX < self.x + self.w and self.y < mouseY < self.y + self.h:
            return True
        else: return False
        
def dispInfo():        
    fill(200)
    rect(1420,880, -820, -600)
    fill(0)
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