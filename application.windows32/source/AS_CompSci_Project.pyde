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
    
    global font
    font = loadFont("SansSerif-120.vlw")
    textFont(font, 32)
    
    global hoverButton
    hoverButton = show.Button(1350, 840, 70, 40, font, "Info", 5)
    
    global killButton
    killButton = show.Button(1020, 760, 180, 40, font, "Natural Selection", 10)
    
    global reprButton
    reprButton = show.Button(1020, 840 ,180, 40, font, "Reproduction", 10)
    
    global iterButton
    iterButton = show.Button(1240, 760 ,180, 40, font, "Evolve full generation", 10)
    
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
    controls = """I = Evolve 1 full generation                                                        TAB = Switch between creature and info screens 
U = Evolve generations as fast as possible. Toggle on\off      Y = Evolves a generation every other frame, showing the process. Toggles on\off
"""
    fill(200)
    textFont(font, 14)
    text(controls, 20, 858)
    
    
    if creatScreen:
        show.drawGrid(20, 40, 40, 25, 35, 32, 200, 250)
        show.drawCreatureGrid(generation, 38, height-842)
        
        fill(200)
        textFont(font, 32)
        text("     EVOLUTION SIMULATOR V1.11", 20, 30)
        text("GEN: " + str(genCount), 1200, 30)
        
        if 20 < mouseX < 1420 and 40 < mouseY < 840:
            xIndex = int((mouseX-20)/35)
            yIndex = int((mouseY-8)/32)
            creatureIndex = (40*(yIndex-1) + xIndex)
            show.creatureInfo(generation[creatureIndex], font)
            
        if genCount == 0:
            fill(200)
            rect(width/2-200, height/2-120, 400, 240)
            textFont(font, 32)
            textAlign(CENTER)
            fill(0)
            text(" Welcome to the\n Evolution Simulator\n Press TAB to move\n to the Info screen,\n to get started",width/2, height/2-70)
            textAlign(LEFT)
            
        
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
        infoScreenText()
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
        global generation, genCount
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.naturalSelection(generation)
        genCount += 0.5

        
    if reprButton.check == True:
        global generation, genCount, topFit, botFit, avgFit, types
        generation = genetic_creature.removeFalses(generation)
        generation = genetic_creature.reproduction(generation)
        topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
        types = genetic_creature.getTypes(generation)
        genCount = int(genCount + 0.5)
        
    if iterButton.check == True:
        global generation, genCount, topFit, botFit, avgFit, types
        genetic_creature.updateEnvironment(warmthSlider.value, foodSlider.value, waterSlider.value, weatherSlider.value)
        generation = genetic_creature.genIteration(generation)
        topFit, botFit, avgFit = getVals(generation, topFit, botFit, avgFit)
        types = genetic_creature.getTypes(generation)
        genCount += 1
    updateScreen()

def dispInfo():
    if 1355 < mouseX <1415 and 845 < mouseY < 875: 
        fill(150)
        rect(1420,880, -1320, -600)
        fill(0)
        textFont(font, 14)
        textLeading(10)
        text(
         """Info\n
\n
This page shows information about the creatures, and allows you to change\n
their environment. The creatures with the greatest fitness are more likely\n
to survive each generation. The surviving creatures then replicate themselves,\n
and their attributes mutate each time they reproduce, like in evolution. The\n
fitness of each creature is then worked out from its attributes, taking into\n
account the environment settings.\n
\n
"""
         , 800, 320)
        text(
         """How Attributes\n
Affect Creatures:\n

Creature Number:\n
No effect on fitness\n

Fitness:\n
This is the most important attribute of a creature, it is calculated from the rest of its\n
attributes, and is what decides whether or not the creature survives a generation.\n

Size: This attribute affects fitness, and also a creature's other statistics cannot exceed\n
it's size, just like how a single-celled organism wouldn't be able to have advanced vision\n
or be extremely strong. A creature's size is show by how large it is on the creature screen.\n

Strength: This attribute affects fitness. The amount of food in the environment affects how\n
useful this attribute is, more food means strength is more useful. In the creature screen, a\n
creature that has a more RED body will exhibit a high strength.\n

Perception: This attribute affects fitness. For a higher fitness, perception requires high\n
food and water availability. In the creature screen, a more GREEN body on a creature will\n 
exhibit higher perception.\n

Intelligence: This attribute affects fitness. Lots of water and high intelligence will make\n
for a fitter creature. An intelligent creature's body will appear BLUE.\n

Endurance: This attribute affects fitness. A high endurance will decrease the fitness given\n
from a creature's size, but will greatly increase the creature's fitness if the environment\n
lacks an abundance of food. In the creature screen, a creature with more EDGES will have a\n
greater endurance attribute.

\n
"""
         , 120, 320)
    else: updateScreen()

def infoScreenText():
    textFont(font, 32)
    fill(200)
    
    if genCount == 0:
        text("""This is the info screen, press the Natural Selection button on the
bottom to cause Natural selection.""", 400, 600)
        
    elif genCount == 0.5:
        text("""This is the info screen, press the Natural Selection button on the
bottom to cause Natural selection.""", 400, 600)
        textFont(font, 24)
        text("""Well done! Now check the creature screen by pressing TAB to see the surviving creatures.
They are sorted from most likely to survive, to least likely. Maybe some of the better
adapted creatures got unlucky though? Evolution is greatly influenced by probability,
after all.
Next, press the Reproduce button on the bottom to cause the survivors to
reproduce, passing down their genes to the next generation.""", 40, 680)
        
    elif genCount == 1:
        textFont(font, 32)
        text("""Great! Now try pressing U to get this process to happen as fast as
possible, or Y to show each step of it.""", 400, 600)
        
    elif 15 > genCount > 1:
        textFont(font, 32)
        text("""Great! Now try pressing U to get this process to happen as fast as
possible, or Y to show each step of it.""", 400, 600)
        textFont(font, 24)
        text("""Now evolution has started! You may notice certain creature types (species)
becoming more dominant in the creature screen! This is because they are better adapted
to their environment. You can recognise species by their background colour. You may notice
a new species with a large mutation could be much better adapted (shown by
"FITNESS"), then you'll observe this species become dominant!""", 40, 680)
    else:
        textFont(font, 32)
        text("""Congratulations on completing the tutorial! Have fun watching evolution
in action!""", 400, 600)
        textFont(font, 24)
        text("""You can pause the simulation by pressing the same button it was started with,
and change the creature's environment settings. You may see their average fitness change,
however, over time evolution will always push them towards being more adapted.
For more information on how the creatures will adapt to each environmental
change, you can hover over the 'info' button in the bottom right.""", 40, 680)
    

    
#This updates the 'maxFit' 'midFit' and 'minFit' arrays which the fitness graph uses
def getVals(generation, top, bot, mid):
    top.append(generation[0].fitness)
    bot.append(generation[-1].fitness)
    mid.append(generation[len(generation)/2].fitness)
    return top, bot, mid
