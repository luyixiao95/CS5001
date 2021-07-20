#Start and end Scene

from graphics import *

def backBottom(win):
    backBottomPic = Rectangle(Point(1.5, 1), Point(2.5, 1.5))
    backBottomPic.setFill('gray')
    backBottomText = Text(Point(2, 1.25), 'Back')

    backBottomPic.draw(win)
    backBottomText.draw(win)

    while True:
        currentClick = win.getMouse()
        currX = currentClick.getX()
        currY = currentClick.getY()

        if currX > 1.5 and currX < 2.5 and currY > 1 and currY < 1.5:
            backBottomPic.undraw()
            backBottomText.undraw()
            break

        else:
            pass

def highScoreCorner(win, highScore):
    hSC = []
    hornorPic = Rectangle(Point(0, 0), Point(4, 4))
    hornorPic.setFill('black')
    hornorMess = Text(Point(2, 3.5), 'High Score')
    hornorMess.setSize(30)
    hornorMess.setStyle('bold')
    hornorMess.setTextColor('white')

    texttitle1 = Text(Point(2, 2.6), '25 Blocks mode')
    text1 = Text(Point(2, 2.4), highScore[0])
    text2 = Text(Point(2, 2.2), str(highScore[1]) + ' seconds')
    texttitle2 = Text(Point(2, 1.8), '50 Blocks mode')
    text3 = Text(Point(2, 1.6), highScore[2])
    text4 = Text(Point(2, 1.4), str(highScore[3]) + ' seconds')
    texttitle3 = Text(Point(2, 1), 'Infinite mode')
    text5 = Text(Point(2, 0.8), highScore[4])
    text6 = Text(Point(2, 0.6), str(highScore[5]) + ' points')
    text1.setTextColor('white')
    text2.setTextColor('white')
    text3.setTextColor('white')
    text4.setTextColor('white')
    text5.setTextColor('white')
    text6.setTextColor('white')
    text1.setSize(12)
    text2.setSize(12)
    text3.setSize(12)
    text4.setSize(12)
    text5.setSize(12)
    text6.setSize(12)

    texttitle1.setTextColor('white')
    texttitle2.setTextColor('white')
    texttitle3.setTextColor('white')
    texttitle1.setStyle('bold')
    texttitle2.setStyle('bold')
    texttitle3.setStyle('bold')
    texttitle1.setSize(18)
    texttitle2.setSize(18)
    texttitle3.setSize(18)
    
    hSC.append(hornorPic)
    hSC.append(hornorMess)
    hSC.append(text1)
    hSC.append(text2)
    hSC.append(text3)
    hSC.append(text4)
    hSC.append(text5)
    hSC.append(text6)
    hSC.append(texttitle1)
    hSC.append(texttitle2)
    hSC.append(texttitle3)

    for i in range(len(hSC)):
        hSC[i].draw(win)

    backBottomPic = Rectangle(Point(3,0.4), Point(3.8,0.8 ))
    backBottomPic.setFill('gray')
    backBottomText = Text(Point(3.4, 0.6), 'Back')

    backBottomPic.draw(win)
    backBottomText.draw(win)

    while True:
        currentClick = win.getMouse()
        currX = currentClick.getX()
        currY = currentClick.getY()

        if currX > 3 and currX < 3.8 and currY > 0.2 and currY < 1:
            backBottomPic.undraw()
            backBottomText.undraw()
            for i in range (len(hSC)):
                hSC[i].undraw()
            break

        else:
            pass
    
def quitScene(win):
    qSC = []

    quitPic = Rectangle(Point(0, 0), Point(4, 4))
    quitPic.setFill('black')
    quitMess = Text(Point(2,3), 'Are you sure?')
    quitMess.setTextColor('white')
    quitMess.setSize(20)

    yesBar = Rectangle(Point(1.2, 2), Point(1.6, 2.3))
    yesBar.setFill('gray')
    yesText = Text(Point(1.4, 2.15), 'Y')

    noBar = Rectangle(Point(2.4, 2), Point(2.8, 2.3))
    noBar.setFill('gray')
    noText = Text(Point(2.6, 2.15), 'N')

    qSC.append(quitPic)
    qSC.append(quitMess)
    qSC.append(yesBar)
    qSC.append(noBar)
    qSC.append(yesText)
    qSC.append(noText)

    for i in range(len(qSC)):
        qSC[i].draw(win)

    while True:
        choiseClick = win.getMouse()
        choiseX = choiseClick.getX()
        choiseY = choiseClick.getY()

        if choiseY > 2 and choiseY < 2.3:

            if choiseX > 1.2 and choiseX < 1.6:
                win.close()
                break

            elif choiseX > 2.4 and choiseX < 2.8:
                for i in range(len(qSC)):
                    qSC[i].undraw()
                break

            else:
                pass


        else:
            pass

    

    


def startScene(win, highScore):
    startScene = []
    startPic = Rectangle(Point(0, 0), Point(4, 4))
    startPic.setFill('black')
    startMess = Text(Point(2,3.5), 'Dont Touch the White Block!')
    startMess.setTextColor('white')
    startMess.setSize(20)
    start25Game = Rectangle(Point(1, 1.6), Point(3, 1.9))
    start25Game.setFill('gray')
    start25GameMess = Text(Point(2, 1.75), 'Start with 25 Blocks')
    start25GameMess.setSize(12)
    start50Game = Rectangle(Point(1, 1.1), Point(3, 1.4))
    start50Game.setFill('gray')
    start50GameMess = Text(Point(2, 1.25), 'Start with 50 Blocks')
    start50GameMess.setSize(12)
    startInfGame = Rectangle(Point(1, 0.6), Point(3, 0.9))
    startInfGame.setFill('gray')
    startInfGameMess = Text(Point(2, 0.75), 'Endless Timed Mode')
    startInfGameMess.setSize(12)

    startScene.append(startPic)
    startScene.append(startMess)
    startScene.append(start25Game)
    startScene.append(start50Game)
    startScene.append(startInfGame)
    startScene.append(start25GameMess)
    startScene.append(start50GameMess)
    startScene.append(startInfGameMess)

    highScoreBar = Rectangle(Point(2.6, 3), Point(3.8, 3.3))
    highScoreBar.setFill('gray')
    highScoreText = Text(Point(3.2, 3.15), 'See High Score')

    quitBar = Rectangle(Point(0.2, 3), Point(1.4, 3.3))
    quitBar.setFill('gray')
    quitText = Text(Point(0.8, 3.15), 'Quit')
    
    startScene.append(highScoreBar)
    startScene.append(highScoreText)
    startScene.append(quitBar)
    startScene.append(quitText)

    for i in range(len(startScene)):
        startScene[i].draw(win)

    while True:
        choiseClick = win.getMouse()
        choiseX = choiseClick.getX()
        choiseY = choiseClick.getY()

        if choiseX > 1 and choiseX < 3:

            if choiseY > 1.6 and choiseY < 1.9:
                for i in range(len(startScene)):
                    startScene[i].undraw()
                return 25

            elif choiseY > 1.1 and choiseY < 1.4:
                for i in range(len(startScene)):
                    startScene[i].undraw()
                return 50

            elif choiseY > 0.6 and choiseY < 0.9:
                for i in range(len(startScene)):
                    startScene[i].undraw()
                return 'infinite'
            
        elif choiseY > 3 and choiseY < 3.3:
            if choiseX > 2.6 and choiseX < 3.8:
                highScoreCorner(win, highScore)
                pass
            elif choiseX > 0.2 and choiseX < 1.4:
                quitScene(win)
                pass
                

            else:
                pass

        else:
            pass

def gameScene(win):
    for i in range(5):
        step_LineX = Line(Point(i ,0), Point(i, 4))
        step_LineX.setWidth(3)
        step_LineX.draw(win)

    for i in range(5):
        step_LineY = Line(Point(0, i), Point(4, i))
        step_LineY.setWidth(3)
        step_LineY.draw(win)

def endScene(win):
    endPic = Rectangle(Point(0,0), Point(4,4))
    endPic.setFill('black')
    endMess = Text(Point(2,2), 'You Failed!')
    endMess.setTextColor('white')
    endMess.setSize(20)

    endPic.draw(win)
    endMess.draw(win)

    backBottom(win)

    endPic.undraw()
    endMess.undraw()

def winScene(win, amount, score):
    endPic = Rectangle(Point(0,0), Point(4,4))
    endPic.setFill('black')
    endMess = Text(Point(2,2), 'You Finished ' + str(amount) + ' Blocks in\n'
                   + str(score) + ' Seconds!')
    endMess.setTextColor('white')
    endMess.setSize(17)

    endPic.draw(win)
    endMess.draw(win)

    backBottom(win)

    endPic.undraw()
    endMess.undraw()


def endSceneTime(win, score):
    endPic = Rectangle(Point(0,0), Point(4,4))
    endPic.setFill('black')
    endMess = Text(Point(2,2.5), 'You Scored ' + str(score) + '!')
    endMess.setTextColor('white')
    endMess.setSize(20)

    endPic.draw(win)
    endMess.draw(win)

    backBottom(win)
    
    endPic.undraw()
    endMess.undraw()

def inputName(win):

    inputPic = Rectangle(Point(0,0), Point(4,4))
    inputPic.setFill('black')
    inputMess = Text(Point(2,3), 'You beat the highscore!\nPlease enter your name!')
    inputMess.setTextColor('white')
    inputMess.setSize(17)
    inputEnter = Entry(Point(2, 2), 15)
    inputEnter.setText('player')

    inputPic.draw(win)
    inputMess.draw(win)
    inputEnter.draw(win)

    conBottomPic = Rectangle(Point(1.5, 1), Point(2.5, 1.5))
    conBottomPic.setFill('gray')
    conBottomText = Text(Point(2, 1.25), 'Conform')

    conBottomPic.draw(win)
    conBottomText.draw(win)

    while True:
        currentClick = win.getMouse()
        currX = currentClick.getX()
        currY = currentClick.getY()

        if currX > 1 and currX < 2 and currY > 1 and currY < 1.5:
            conBottomPic.undraw()
            conBottomText.undraw()
            inputEnter.undraw()
            inputPic.undraw()
            inputMess.undraw()
            return inputEnter.getText()

        else:
            pass



