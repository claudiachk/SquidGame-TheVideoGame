"""
Claudia Cheuk
Squid Game: The Video Game
"""

startMode = False
rlgl = False
dalgona = False
tow = False
failD = False
failR = False
clickOn = False
win = False

charPos = [100,600]
charDir = 20
towPos = [100,267]
towDir = -10
oppPos = [-1000,267]
oppDir = 20
startTime = random(1500,3000)
dotPos = []
lastTime = 1000
lastTimeTow = 1000
randomCutOff = random(1000,2000)
rectPos = [700,350]
rectDir = 10

def setup():
    size(1400,800)
    imageMode(CENTER)
    
    global regFont, landingBG, rlglBG, sand, runChar, midChar, statTow, normView, flippedView, sideView, rectDalgona, crDalgona, blood
    landingBG = loadImage("landingpagebg.jpeg")
    rlglBG = loadImage("wheat field.jpeg")
    sand = loadImage("sand.jpeg")
    runChar = loadImage("run.png")
    midChar = loadImage("mid.png")
    normView = loadImage("norm.png")
    flippedView = loadImage("flipped.png")
    rectDalgona = loadImage("rectDalgona.png")
    crDalgona = loadImage("crDalgona.png")
    blood = loadImage("blood.png")
    statTow = loadImage("stat.png")
    
    bodyFont = createFont("GameOfSquids-1GMVL.ttf", 30)
    regFont = createFont("SourceCodePro-BoldIt.otf",20)
    
    textFont(bodyFont)
    textAlign(CENTER, CENTER)
    rectMode(CENTER)
    noStroke()

    
def draw():
    global rectPos, rectDir, lastTimeTow, startMode, rlgl, dalgona, tow, charPos, startTime, failD, failR, lastTime, randomCutOff, win, towPos, towDir, oppPos, oppDir
    
    #landing page
    startMode == True
    textSize(30)
    fill(255)
    image(landingBG, width/2, height/2-100, width, height)
    text("The VidEo GAme", width/2+180, height/2+120)
    text("Choose your game:", width/2, height-150)
    
    #red light green light hover button
    if mouseX >= 0 and mouseX <= width/3 and mouseY >= 700:
        fill(255)
        rect(width/6, 750,width/3,100)
        textSize(20)
        fill(174,12,28)
        text("REd Light, GrEEn Light", width/6, height-55)
        if mousePressed:
            rlgl = True
    else:
        fill(174,12,28)
        rect(width/6, 750,width/3,100)
        textSize(20)
        fill(255)
        text("REd Light, GrEEn Light", width/6, height-55)
    
    #dalgona hover button
    if mouseX >= width/3 and mouseX <= width*2/3 and mouseY >= 700:
        fill(255)
        rect(width/2,750,width/3,100)
        fill(48,233,218)
        text("Dalgona/Ppopgi",width/2,height-55)
        if mousePressed:
            dalgona = True
    else:
        fill(48,233,218)
        rect(width/2,750,width/3,100)
        fill(255)
        text("Dalgona/Ppopgi",width/2,height-55)
    
    #tug of war button
    if mouseX >= width*2/3 and mouseX <= width and mouseY >= 700:
        fill(255)
        rect(width-width/6, 750, width/3, 100)
        fill(39,42,82)
        text("Tug of War", width*5/6, height-55)
        if mousePressed:
            tow = True
    else:
        fill(39,42,82)
        rect(width-width/6, 750, width/3, 100)
        fill(255)
        text("Tug of War", width*5/6, height-55)

    #red light green light gameplay
    if rlgl == True:
        image(rlglBG, width/2, height/2, width, height)
        image(sand, width/2, height-height/8, width, height/4)
        push()
        fill(255)
        textFont(regFont)
        text("Welcome to red light green light. Press spacebar to run", width/2, height/9)
        text("while avoiding being caught by the doll. Release to stand still.", width/2, height/9+25)
        text("Cross the red line and tag the doll to win.", width/2, height/9+50)
        pop()
        #return home button
        if failR == False:
            push()
            if mouseX in range (64, 216) and mouseY in range (81, 194):
                fill(255,0,0)
                if mousePressed:
                    rlgl = False
                    startMode = True
            else:
                fill(255)
            text("RETURN HOME", width/10, height/10)
            pop()
        currentTime = millis()
        if currentTime - lastTime > randomCutOff:
            randomCutOff = random(1500,3000)
            lastTime = currentTime
            image(flippedView, width/2, height/2, width, height-200)
            if keyPressed:
                failR = True
        else:
            image(normView, width/2, height/2, width, height-200)
        pushStyle()
        fill(255,0,0,99)
        rect(1150,height, 5, 400)
        popStyle()
        if keyPressed and key == ' ':
            image(runChar, charPos[0], charPos[1], 130,150)
            charPos[0] += charDir
        else:
            image(midChar, charPos[0], charPos[1], 130, 150)
        if charPos[0] > 1150:
            win = True
        
    #dalgona gameplay
    if dalgona == True:
        image(sand,width/2, height/2, width, height)
        image(rectDalgona, width/2, height/2, width/3, width/3)
        push()
        fill(0)
        textFont(regFont)
        text("Welcome to dalgona. Free the dalgona by piercing the dalgona", width/2, height/9)
        text("with your mouse as the needle by clicking on the outline of the shape.", width/2, height/9+25)
        text("Proceed with caution, if it goes out of bound, your dalgona will break and you will fail.", width/2, height/9+50)
        pop()
        #return home button
        if failD == False:
            push()
            if mouseX in range (64, 216) and mouseY in range (81, 194):
                fill(255,0,0)
                if mousePressed:
                    dalgona = False
                    startMode = True
            else:
                fill(50)
            text("RETURN HOME", width/10, height/10)
            pop()
        push()
        fill(150)
        triangle(mouseX-5, mouseY-100, mouseX, mouseY, mouseX+5, mouseY-100)
        pop()
        if clickOn == True:
            for _dot in dotPos:
                push()
                fill(95, 69, 16, 90)
                ellipse(_dot[0], _dot[1], 10,10)
                pop()
        if len(dotPos) > 120:
            win = True
        if win == False and mousePressed and len(dotPos) > 0:
            if (mouseY > 527 or mouseY < 276) or mouseY in range (296,507):
                if mouseX > 826 or mouseX < 574 or mouseX in range (594, 806):
                    failD = True
    
    #tug of war gameplay
    if tow == True:
        background(50)
        push()
        fill(100)
        rectMode(CORNER)
        rect(0, height/2, width/3, height/5)
        rect(width*2/3, height/2, width/3, height/5)
        fill(255,255,0)
        rect(0, height/2+50, width/3, height/10)
        rect(width*2/3, height/2+50, width/3, height/10)
        pop()
        push()
        fill(100,100,10,90)
        rect(width/2, height/2-55, width, 5)
        pop()
        #return home button
        if failR == False:
            push()
            if mouseX in range (64, 216) and mouseY in range (81, 194):
                fill(255,0,0)
                if mousePressed:
                    tow = False
                    startMode = True
            else:
                fill(255)
            text("RETURN HOME", width/10, height/10)
            pop()
        push()
        fill(255)
        textFont(regFont)
        text("Welcome to tug of war. You are on the blue team on the left.", width/2, height/9)
        text("Press spacebar to tug on the rope. The quickest team to get", width/2, height/9+25)
        text("the red flag past the edge of their podium wins.", width/2, height/9+50)
        pop()
        fill(0,0,255)
        triangle(width/5-30, height/5, width/5, height/4, width/5+30, height/5)
        for i in range(0, 5):
            for j in range(0, 5):
                push()
                imageMode(CORNER)
                translate((i+1)*50, 0)
                image(statTow,towPos[0],towPos[1],100,180)
                pop()
        if keyPressed and key == ' ':
            towPos[0] += towDir
        for i in range(0, 5):
            for j in range(0, 5):
                push()
                imageMode(CORNER)
                translate((i+1)*50, 0)
                scale(-1,1)
                image(statTow,oppPos[0],oppPos[1],100,180)
                pop()
        currentTime = millis()
        if keyPressed > 0:
            if currentTime - lastTimeTow > randomCutOff:
                randomCutOff = random(1500,3000)
                lastTimeTow = currentTime
                oppPos[0] -= oppDir
        if keyPressed and key == ' ':
            rectPos[0] -= rectDir
        elif oppPos[0] > towPos[0]:
            rectPos[0] += rectDir
        fill(255,0,0)
        rect(rectPos[0], rectPos[1], 10, 50)
        if rectPos[0] <= width/3:
            win = True
        elif rectPos[0] >= width*2/3:
            failR = True
        
    #wins
    textSize(40)
    if win == True:
        fill(255)
        text("Congratulations!", width/2, height/4)
        text("You can move on to the nExt round.", width/2, height/4+40)
        push()
        textSize(20)
        print(mouseY)
        if mouseX in range (378,1021) and mouseY in range (292,305):
            fill(255)
            if mousePressed: #restart to home page
                tow = False
                dalgona = False
                rlgl = False
                win = False
                startMode = True
        else:
            fill(255,0,0)
        text("Click to rEturn to home and sElEct new level", width/2, height/4+90)
        pop()
        
    #failed outcomes
    textSize(40)
    #red light green light
    if failR == True:
        image(blood,width/2, height/2, width/2, height/2)
        text("I'm sorry, you have failed.", width/2, height/2)
    #dalgona

    if failD == True:
        image(crDalgona, width/2, height/2, width/3, width/3)
        text("I'm sorry, you have failed.", width/2, height/2)

        
def mousePressed():
    global clickOn, dotPos
    if dalgona == True:
        dotPos.append([mouseX, mouseY])
        clickOn = True
        
    
