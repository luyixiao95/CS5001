# Read high score

def readHighScore():
    highScore = []
    hs = open('HighScore.txt', 'r')
    high_temp = hs.read()
    highScore = high_temp.split(',')
    hs.close()

    if len(highScore) != 6:
        highScore = ['player', '999.99', 'player', '999.99', 'player', '0']
        pass

    else:
        pass

    try:
        highScore[1] = eval(highScore[1])
        highScore[3] = eval(highScore[3])
        highScore[5] = eval(highScore[5])

    except NameError:

        if type(highScore[1]) != type(999.99):
            highScore[1] = 999.99
            pass
            
        elif type(highScore[3]) != type(999.99):
            highScore[3] = 999.99
            pass
        
        elif type(highScore[5]) != type(0):
            highScore[5] = 0
            pass

        else:
            pass

    else:
         pass

    return highScore

def checkScore(score, mode, highScore):
    if mode == 25:
        if score < highScore[1]:
            return True
        else:
            return False

    elif mode == 50:
        if score < highScore[3]:
            return True
        else:
            return False

    elif mode == 'infinite':
        if score > highScore[5]:
            return True
        else:
            return False

def writeHighScore(name, score, mode, highScore):

    if mode == 25:
        highScoreNew = [name, score, highScore[2], highScore[3],
                        highScore[4], highScore[5]]
        pass

    elif mode == 50:
        highScoreNew = [highScore[0], highScore[1], name, score,
                        highScore[4], highScore[5]]
        pass

    elif mode == 'infinite':
        highScoreNew = [highScore[0], highScore[1], highScore[2], highScore[3],
                        name, score]
        pass

    hs = open('HighScore.txt', 'w')
    highScoreNew[1] = str(highScoreNew[1])
    highScoreNew[3] = str(highScoreNew[3])
    highScoreNew[5] = str(highScoreNew[5])

    strScore = ','.join(highScoreNew)
    hs.write(strScore)

    return highScoreNew


    
