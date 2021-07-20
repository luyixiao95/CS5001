# Don't touch white blocks

from graphics import *
from actions import *
from scene import *
from timed import *
from scoreCheck import *


def main():

    try:
        blockcolor = 'black'

        win = GraphWin('Dont Touch White Blocks', 400, 600)
        win.setCoords(0, 0, 4, 4)
        win.setBackground('white')

        while True:
            highScore = readHighScore()
            gameScene(win)
            amount = startScene(win, highScore)

            if amount == 'infinite':
                score = runTimeMode(win, blockcolor)

                if checkScore(score, amount, highScore) == False:
                    endSceneTime(win, score)
                    pass

                if checkScore(score, amount, highScore) == True:
                    name = inputName(win)
                    highScore = writeHighScore(name, score, amount, highScore)
                    pass

            else:
                start = createStartBB(win)
                bbGroup, locateGroup = createBB(win, amount, blockcolor)
                bbGroup = createEndBB(win, bbGroup, amount)    
                timeini = firstClick(win, locateGroup)

                start[0].setFill('gray')
                start[1].undraw()
                start[0].undraw()
                start[0].draw(win)
                bbAllDown(bbGroup)   

                gameEnd = run_game(win, bbGroup, locateGroup)

                if gameEnd == True:
                    for i in range(amount + 2):
                        bbGroup[i].undraw()
                    endScene(win)
                    pass

                else:
                    timeFin = time.time()
                    for i in range(amount + 2):
                        bbGroup[i].undraw()
                    score = round(timeFin - timeini, 2)

                    if checkScore(score, amount, highScore) == False:
                        winScene(win, amount, score)
                        pass

                    if checkScore(score, amount, highScore) == True:
                        name = inputName(win)
                        highScore = writeHighScore(name, score, amount, highScore)
                        pass

    except GraphicsError:
        print('Goodbye')



if __name__ == '__main__':
    main()
