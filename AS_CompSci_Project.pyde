__author__ = 'George'
#screen = 2880 x 1800

import random, time, genetic_creature, show, funcs
genLen = 1000
generation = genetic_creature.initialise(genLen)
genCount = 0
creatScreen = True
genASAP = False
showGenASAP = False
showGenStep = 0

topFit, botFit, avgFit = [], [], []
types = genetic_creature.getTypes(generation)

def setup():
    fullScreen()
    background(21, 34, 56)
    noiseDetail(12)
    
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
    
    global warmthSlider 
    warmthSlider = show.Slider(850, 300, 400, font, "Warmth")
    
    global foodSlider 
    foodSlider = show.Slider(850, 370, 400, font, "Food")
    
    global waterSlider 
    waterSlider = show.Slider(850, 440, 400, font, "Water")
    
    global weatherSlider 
    weatherSlider = show.Slider(850, 510, 400, font, "Weather")
    updateScreen()

def draw():
    if creatScreen:
        if 10 < mouseX < 1430 and 30 < mouseY < height or hoverButton.check == True:
            updateScreen()

    if killButton.check == True or reprButton.check == True: 
        cursor(HAND)    
    elif hoverButton.check == True:
            dispInfo()
            cursor(HAND)
    else: cursor(ARROW)
    
    if genASAP == True:
        global generation, genCount, topFit, botFit, avgFit, types
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.genIteration(generation)
        topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
        types = genetic_creature.getTypes(generation)
        
        genCount += 1
        updateScreen()

    if showGenASAP == True:
        global generation, genCount, showGenStep, topFit, botFit, avgFit
        if showGenStep == 0:
            genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
            generation = genetic_creature.naturalSelection(generation)
            showGenStep = 1
            updateScreen()
            
        elif showGenStep == 1:
            generation = genetic_creature.reproduction(genetic_creature.removeFalses(generation))
            topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
            types = genetic_creature.getTypes(generation)
            showGenStep = 0
            genCount += 1
            updateScreen()
        updateScreen()
        
    if mousePressed:
        updateScreen()

def updateScreen():
    clear()
    background(21, 34, 56)
    controls = """I = Evolve 1 generation
U = Toggle evolve ASAP      Y = Toggle show evolution ASAP
"""
    fill(200)
    textFont(font, 14)
    text(controls, 20, 858)
    
    
    if creatScreen:
        show.drawGrid(20, 40, 40, 25, 35, 32, 200, 250)
        show.drawCreatureGrid(generation, font, 38, height-842)
        
        fill(200)
        textFont(font, 32)
        text("     EVOLUTION SIMULATOR V1", 20, 30)
        text("GEN: " + str(genCount), 1200, 30)
        
        if 20 < mouseX < 1420 and 40 < mouseY < 840:
            xIndex = int((mouseX-20)/35)
            yIndex = int((mouseY-8)/32)
            creatureIndex = (40*(yIndex-1) + xIndex)
            show.creatureInfo(generation[creatureIndex], font)
        
    else:
        fill(200)
        textFont(font, 52)
        text("     EVOLUTION\nSIMULATOR V1", 1060, 60)
        text("GEN: " + str(genCount), 840, 186)
        
        
        show.showFitGraph(font,topFit, botFit, avgFit, generation, "Fitness:  ")
        show.showTypeChart(180, 470, 300, types, font)
            
        warmthSlider.show()
        foodSlider.show()
        waterSlider.show()
        weatherSlider.show()
        stroke(200)
        
        
            
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
        global generation, genCount, topFit, botFit, avgFit, types
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.genIteration(generation)
        topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
        types = genetic_creature.getTypes(generation)
        genCount += 1
        updateScreen()
    if key in ("U", "u"):
        global genASAP
        genASAP = not genASAP
        
    if key in ("Y", "y"):
        if showGenStep == 0:
            global showGenASAP
            showGenASAP = not showGenASAP
        else:
            global showGenASAP, generation
            showGenASAP = not showGenASAP
            generation = genetic_creature.reproduction(genetic_creature.removeFalses(generation))
            
def mouseClicked():
    
    if killButton.check == True:
        global generation
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.naturalSelection(generation)

        
    if reprButton.check == True:
        global generation, genCount
        generation = genetic_creature.removeFalses(generation)
        generation = genetic_creature.reproduction(generation)
        genCount += 1
        
    if iterButton.check == True:
        global generation, genCount, topFit, botFit, avgFit
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.genIteration(generation)
        topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
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
    if 1355 < mouseX <1415 and 845 < mouseY < 875: 
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
    else: updateScreen()
    
def getVals(generation, top, bot, mid):
    top.append(generation[0].fitness)
    bot.append(generation[-1].fitness)
    mid.append(generation[len(generation)/2].fitness)
    return top, bot, mid