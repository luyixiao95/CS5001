#Luyi Xiao
#CS 5001 & CS 5003
#Final, creating a small game - tetris using graphics.py


import graphicsPlus as gr
#To creat the high score page
def h_scorepage():
    win = gr.GraphWin("Highest Score", 400, 800)
    hs = open("HighestScore.txt", "r")
    highest = str(hs.read())
    word = gr.Text(gr.Point(200, 400), "Highest Score: " + highest)
    word.setFace("arial")
    word.setStyle("bold")
    word.setSize(20)
    word.draw(win)


#To create the frontpage of the game
def front():
    rungame = False
    win = gr.GraphWin("Tetris", 400, 800)
    title = gr.Text(gr.Point(200, 200), "Final Project: Tetris")
    title.setFace("arial")
    title.setStyle("bold")
    title.setSize(28)
    title.setTextColor("blue")

    button1 = gr.Rectangle(gr.Point(100, 350), gr.Point(300, 450))
    button1.setFill("gray")
    starter = gr.Text(gr.Point(200, 400), "Start Game")
    starter.setFace("arial")
    starter.setStyle("italic")
    starter.setSize(20)

    coder = gr.Text(gr.Point(200, 700), "By Luyi Xiao")
    coder.setFace("times roman")
    coder.setStyle("normal")
    coder.setSize(12)


    button2 = gr.Rectangle(gr.Point(100, 550), gr.Point(300, 650))
    button2.setFill("gray")
    Highest = gr.Text(gr.Point(200, 600), "Highest Score")
    Highest.setFace("arial")
    Highest.setStyle("italic")
    Highest.setSize(20)

    title.draw(win)
    coder.draw(win)
    button1.draw(win)
    starter.draw(win)
    button2.draw(win)
    Highest.draw(win)

    click_x = 0
    click_y = 0

    #while loop to detect when click the botton rightly

    while True:
        click = win.getMouse()
        click_x = click.getX()
        click_y = click.getY()
        if click_x > 100 and click_x < 300 and click_y >350 and click_y < 450:
            rungame = True
            win.close()
            break


        elif click_x > 100 and click_x <300 and click_y > 550 and click_y <650:
            h_scorepage()

            

    
    return rungame
    

if __name__ == "__main__":
    a = front()
    print(a)