import graphicsPlus as gr
def volcano_init(x, y, scale):
    list=[gr.Point(30, 30), gr.Point(40, 100), gr.Point(200, 200)]
    ploygon = gr.Polygon(list)
    ploygon.setFill("red")

    return ploygon


def main():
    win = gr.GraphWin("win", 400, 400)
    t = volcano_init(100, 30, 1)
    t.draw(win)
    win.getMouse()
    win.close()

main()

