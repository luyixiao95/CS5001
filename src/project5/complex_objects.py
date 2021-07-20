#Luyi Xiao
#CS 5001 & 5003
#Feb 13, 2020 complex_shape.py
#Build a new scene using graphicPlus:
import graphicsPlus as gr
import time
import random

#https://drive.google.com/file/d/1wNR6T5wjN-pXzsjYo1NeGw8lE3nXIzC6/view?usp=sharing
#define the draw function to simplify the functions below
def draw(list, win):
    for item in list:
        item.draw(win)

#define some new objects in project 5:

#define a house function, contains house_base, window, door, knob, chimney and roof
def house_init(x, y, scale):
    #house_base
    house_base = gr.Rectangle(gr.Point(x+0*scale, y-0*scale), gr.Point(x+40*scale, y-40*scale))
    house_base.setFill(gr.color_rgb(255, 204, 50))

    #window
    window = gr.Rectangle(gr.Point(x+5*scale, y-20*scale), gr.Point(x+15*scale, y-28*scale))
    window.setFill(gr.color_rgb(255, 102, 153))

    #door
    door = gr.Rectangle(gr.Point(x+29*scale, y-0*scale), gr.Point(x+38*scale, y-16*scale))
    door.setFill(gr.color_rgb(255, 153, 102))

    #knob
    knob = gr.Circle(gr.Point(x+30*scale, y-8*scale), 1*scale)
    knob.setFill(gr.color_rgb(153, 255, 255))
    #chimney
    chimney = gr.Rectangle(gr.Point(x+26*scale, y-53*scale), gr.Point(x+28*scale, y-47*scale))
    chimney.setFill(gr.color_rgb(102, 153, 255))

    #roof
    roof_list = [gr.Point(x+0*scale, y-40*scale), gr.Point(x+20*scale, y-55*scale), gr.Point(x+40*scale, y-40*scale)]
    roof = gr.Polygon(roof_list)
    roof.setFill(gr.color_rgb(255, 255, 102))
    



    house = [house_base, window, door, knob, chimney, roof]
    return house

#build a subway that contains train and rail 
#bulid the rail function first

def rail_init(x, y, scale):

    #rail
    rail = gr.Rectangle(gr.Point(x+0*scale, y-165*scale), gr.Point(x+500*scale, y-160*scale))
    rail.setFill(gr.color_rgb(99, 184, 255))
    rail.setOutline(gr.color_rgb(99, 184, 255))
    rail_list = [rail]

    #Using list to store the positio of five pillars that stands for the rail
    pillar_point_list = [[28*scale, 160*scale, 35*scale, 135*scale],
    [128*scale, 160*scale, 135*scale, 135*scale], [228*scale, 160*scale, 235*scale, 135*scale],
    [328*scale, 160*scale, 335*scale, 135*scale], [428*scale, 160*scale, 435*scale, 135*scale]
    ]

    #use for loop to draw the five pillars
    for sublist in pillar_point_list:
        pillar = gr.Rectangle(gr.Point(x+sublist[0], y-sublist[1]), gr.Point(x+sublist[2], y-sublist[3]))
        pillar.setFill(gr.color_rgb(139, 35, 35))
        pillar.setOutline(gr.color_rgb(139, 35, 35))
        rail_list.append(pillar)

    return rail_list
    

#build the train with two carriages and certain elements
def train_init(x, y, scale):
    #build the carriages of the train
    #carriage 1 with window 1, window 2 and door 1
    carriage1 = gr.Rectangle(gr.Point(x+0*scale, y-185*scale), gr.Point(x+40*scale, y-165*scale))
    carriage1.setFill(gr.color_rgb(238, 180, 180))
    carriage1.setOutline(gr.color_rgb(238, 180, 180))

    window1 = gr.Rectangle(gr.Point(x+5*scale, y-175*scale), gr.Point(x+13*scale, y-170*scale))
    window1.setFill(gr.color_rgb(224, 238, 238))
    window1.setOutline(gr.color_rgb(224, 238, 238))

    

    window2 = gr.Rectangle(gr.Point(x+17*scale, y-175*scale), gr.Point(x+25*scale, y-170*scale))
    window2.setFill(gr.color_rgb(224, 238, 238))
    window2.setOutline(gr.color_rgb(224, 238, 238))


    door1= gr.Rectangle(gr.Point(x+30*scale, y-178*scale), gr.Point(x+35*scale, y-167*scale))
    door1.setFill(gr.color_rgb(255, 228, 181))
    door1.setOutline(gr.color_rgb(255, 228, 181))


    #build the carriages 2 with window3, window4 and door2
    carriage2 = gr.Rectangle(gr.Point(x+50*scale, y-185*scale), gr.Point(x+90*scale, y-165*scale))
    carriage2.setFill(gr.color_rgb(123, 104, 238))
    carriage2.setOutline(gr.color_rgb(123, 104, 238))


    window3 = gr.Rectangle(gr.Point(x+55*scale, y-175*scale), gr.Point(x+63*scale, y-170*scale))
    window3.setFill(gr.color_rgb(224, 238, 238))
    window3.setOutline(gr.color_rgb(224, 238, 238))


    window4 = gr.Rectangle(gr.Point(x+67*scale, y-175*scale), gr.Point(x+75*scale, y-170*scale))
    window4.setFill(gr.color_rgb(224, 238, 238))
    window4.setOutline(gr.color_rgb(224, 238, 238))


    door2 = gr.Rectangle(gr.Point(x+80*scale, y-178*scale), gr.Point(x+85*scale, y-167*scale))
    door2.setFill(gr.color_rgb(95, 158, 160))
    door2.setOutline(gr.color_rgb(95, 158, 160))

    #build a linkage of two different carriages
    link = gr.Rectangle(gr.Point(x+40*scale, y-178*scale), gr.Point(x+50*scale, y-173*scale))
    link.setFill(gr.color_rgb(139, 139, 131))
    link.setOutline(gr.color_rgb(139, 139, 131))
    #build a headlight
    headlight = gr.Oval(gr.Point(x+90*scale, y-185*scale), gr.Point(x+92*scale, y-180*scale))
    headlight.setFill(gr.color_rgb(50, 205, 50))
    headlight.setOutline(gr.color_rgb(50, 205, 50))
    
    #conclude all elements of trains to a list
    train = [carriage1, window1, window2, door1, carriage2, window3, window4, door2, link, headlight]

    return train

def newvol_init(x, y, scale):

    #draw the root of the volcano firstly
    new_root_list =[gr.Point(x+125*scale, y-200*scale), gr.Point(x+137*scale, y-217*scale),
    gr.Point(x+147*scale, y-237*scale), gr.Point(x+152*scale, y-257*scale),   #from 161,391
    gr.Point(x+167*scale, y-257*scale), gr.Point(x+182*scale, y-217*scale),
    gr.Point(x+197*scale, y-200*scale) ]
    new_root = gr.Polygon(new_root_list)
    new_root.setFill(gr.color_rgb(238, 230, 133 ))
    new_root.setOutline(gr.color_rgb(205, 173, 0))
    new_root.setWidth(3)

    volcano = [new_root]
    #draw the ridges of the mountain using line objects
    #set the positions firstly
    ridge_point_list = [[142, 218, 147, 222], [149, 221, 147, 222], [147, 217, 152, 227], 
    [162, 222, 167, 213], [165, 217, 166, 218], [170, 213, 166, 218]
    ]
    #using for loop to draw the ridges
    for sublist in ridge_point_list:
        newsublist = [i *scale for i in sublist]
        ridge = gr.Line(gr.Point(x+newsublist[0], y-newsublist[1]), gr.Point(x+newsublist[2], y-newsublist[3]))
        ridge.setOutline(gr.color_rgb(205, 173, 0))
        ridge.setWidth(3)
        volcano.append(ridge)

    

    return volcano


#draw two trees that contains trunk and bush
def tree_init(x, y, scale):

    #draw the trunk of the tree
    trunk1 = gr.Line(gr.Point(x+130*scale, y+30*scale), gr.Point(x+130*scale, y-40*scale))
    trunk1.setOutline(gr.color_rgb(102, 51, 51))
    trunk1.setWidth(6*scale)

    #draw the bush of the tree
    bush1 = gr.Oval(gr.Point(x+115*scale, y-40*scale), gr.Point(x+145*scale, y-90*scale))
    bush1.setFill(gr.color_rgb(153, 255, 153))
    bush1.setOutline(gr.color_rgb(153, 255, 153))

    #draw another tree with trunk and bush
    trunk2 = gr.Line(gr.Point(x+165*scale, y+30*scale), gr.Point(x+165*scale, y-40*scale))
    trunk2.setOutline(gr.color_rgb(102, 51, 51))
    trunk2.setWidth(6*scale)

    bush2 = gr.Oval(gr.Point(x+150*scale, y-40*scale), gr.Point(x+180*scale, y-90*scale))
    bush2.setFill(gr.color_rgb(153, 255, 153))
    bush2.setOutline(gr.color_rgb(153, 255, 153))
    tree = [trunk1, bush1, trunk2, bush2]
    return tree

#draw the meadow that contains several grasses
def meadow_init(x, y, scale):
    #list the position of the meadow elements
    meadow_point_list = [ [90, 0, 105, 8], [103, 1, 112, 6], [108, -2, 115, 3], [113, 0, 119, -4],
    [115, 0, 130, 6], [126, 1, 145, 8], [142, 0, 152, 5], [149, 0, 164, 6]
    ]
    meadow = []
    #use for loop to draw the meadow
    for sublist in meadow_point_list:
        newsublist = [i*scale for i in sublist]
        grass = gr.Oval(gr.Point(x+newsublist[0], y-newsublist[1]), gr.Point(x+newsublist[2], y-newsublist[3]))
        grass.setFill(gr.color_rgb(153, 255, 153))
        grass.setOutline(gr.color_rgb(153, 255, 153))
        meadow.append(grass)

    return meadow 

#deine several pieces of clouds
def cloud_init(x, y, scale):
    #list the position of the cloud in a list
    cloud_point_list = [[52, 260, 95, 280], [70, 270, 95, 287], [90, 270, 110, 285], [110, 268, 130, 278]]
    cloud =[]
    # Use for loop to draw the elements of the cloud list
    for sublist in cloud_point_list:
        item = gr.Oval(gr.Point(x+sublist[0], y-sublist[1]), gr.Point(x+sublist[2], y-sublist[3]))
        item.setFill(gr.color_rgb(0, 255, 255))
        item.setOutline(gr.color_rgb(0, 255, 255))
        cloud.append(item)
    return cloud


#define some test functions for complex objects twice with different scales and positions

def test(function1, function2, name):
    win = gr.GraphWin(name, 750, 500)
    shapes1 = function1
    shapes2 = function2
    draw(shapes1, win)
    draw(shapes2, win)
    win.getMouse()
    win.close()



#define the static main scene 
def main():
    win = gr.GraphWin("seasons", 750, 500)
    house = house_init(100, 500, 2)
    draw(house, win)
    
    volcano = newvol_init(100, 850, 3)
    draw(volcano, win)
    
    subway = rail_init(0, 450, 1.5) + train_init(0, 450, 1.5)
    draw(subway, win)

    tree = tree_init(200, 500, 1.5)
    draw(tree, win)

    meadow = meadow_init(240, 500, 1.5)
    draw(meadow, win)

    cloud = cloud_init(200, 350, 1.5)
    draw(cloud, win)
    win.getMouse()
    win.close()

#define move function to simplify the coding
def move(shapes, dx, dy):
    for item in shapes:
        item.move(dx, dy)


#define undraw function to simplify the coding

def undraw(shapes):
    for item in shapes:
        item.undraw()


#define the animated object train
def animate_train(shapes, frame_num, win): #let the train ignites 
    ending = shapes[0].getP1()
    if ending.getX() > 750: #if the train runs out of the scene, it would start again
        move(shapes, -900, 0)
    move(shapes, 20, 0)
    if frame_num %20 == 10:
        shapes[9].setFill("red")
        shapes[9].setOutline("red")
    elif frame_num %20  == 0:
        shapes[9].setFill(gr.color_rgb(50, 205, 50))
        shapes[9].setOutline(gr.color_rgb(50, 205, 50))



#define the animated tree function in the four seasons
def animate_tree(shapes, frame_num, win):

    starting_point = shapes[0].getP1() 
    cross_point = shapes[0].getP2()
    length = starting_point.getY() - cross_point.getY()
    scale = length/70
    x = starting_point.getX()-130*scale
    y = starting_point.getY()-10*scale



    if frame_num % 100 <=25 :
        move(shapes, 0, -scale*0.2)  #let the tree grow in spring, till max 5*scale

    elif frame_num % 100 >25 and frame_num % 100 <50:
        move(shapes, 0, -scale*0.4)   #let the tree grow faster in summer, till max 10*scale
        shapes[1].setFill(gr.color_rgb(51, 204, 102))    #change the color of the bushes to darker green
        shapes[1].setOutline(gr.color_rgb(51, 204, 102))
        shapes[3].setFill(gr.color_rgb(51, 204, 102))
        shapes[3].setOutline(gr.color_rgb(51, 204, 102))

        


    elif frame_num % 100 == 50:    #let the leaves of the tree be yellow in autumn
        shapes[1].setFill(gr.color_rgb(204, 153, 51))
        shapes[1].setOutline(gr.color_rgb(204, 153, 51))
        shapes[3].setFill(gr.color_rgb(204, 153, 51))
        shapes[3].setOutline(gr.color_rgb(204, 153, 51))

        #add some fruit to the tree
        fruit_point_list = [[120, 75, 125, 80], [125, 93, 132, 97], [160, 75, 164, 82], [170, 84, 175, 91]]
        fruit_list = []

        #use for loop to draw the fruits
        for sublist in fruit_point_list:
            newsublist = [i*scale for i in sublist]
            fruit = gr.Oval(gr.Point(x+newsublist[0], y-newsublist[1]), gr.Point(x+newsublist[2], y-newsublist[3]))
            fruit.setFill("red")
            fruit.setOutline("red")
            fruit.draw(win)
            shapes.append(fruit)


    elif frame_num % 100 == 75:   #winter: tree covered with snows
        for i in range(4):        #pop up and undraw the fruit objects in autumn season 
            item = shapes.pop()
            item.undraw()
        shapes[1].setFill(gr.color_rgb(205, 201, 201))  
        shapes[1].setOutline(gr.color_rgb(205, 201, 201))
        shapes[3].setFill(gr.color_rgb(205, 201, 201))
        shapes[3].setOutline(gr.color_rgb(205, 201, 201))


#define the animated meadow function in the four seasons
def animate_meadow(shapes, frame_num, win):
    #get the x, y, scale
    P1 = shapes[0].getP1()
    P2 = shapes[0].getP2()
    y = P1.getY()
    scale = (y - P2.getY())/8
    x = P1.getX()-90*scale

    if frame_num % 100 == 25:   # change the color of the grass and also add some flowers in summer
        for item in shapes:
            item.setFill(gr.color_rgb(51, 204, 102))
            item.setOutline(gr.color_rgb(51, 204, 102))
        
        #7 flowers
        flower_point_list = [[99, 5, 103, 9, (255, 153, 51)], [111, 4, 113, 9, (153, 0, 204)], [116, 3, 121, 6, (238, 174, 238)], 
        [136, 6, 140, 9, (255, 51, 153)], [139, 6, 141, 8, (102, 102, 255)], [145, 5, 148, 8, (137, 104, 205)],
         [154, 4, 160, 7, (255, 204, 153)]]
        
        #for loop to draw the flowers
        for sublist in flower_point_list:
            flower = gr.Oval(gr.Point(x+scale*sublist[0], y-scale*sublist[1]), gr.Point(x+scale*sublist[2], y-scale*sublist[3]))
            color = sublist[4]
            flower.setFill(gr.color_rgb(color[0], color[1], color[2] ))
            flower.setOutline(gr.color_rgb(color[0], color[1], color[2]))
            flower.draw(win)
            shapes.append(flower)

    elif frame_num % 100 == 50: #autumn time the grass turns yellow as well, and the flowers wither
        for i in range(7):
            flower = shapes.pop()
            flower.undraw()
        for grass in shapes:  #change the color of grass
            grass.setFill(gr.color_rgb(255, 193, 37))
            grass.setOutline(gr.color_rgb(255, 193, 37))

    elif frame_num % 100 == 75: #winter: grass withers as well 
        for grass in shapes:
            grass.undraw()

#define the animated cloud function
def animate_cloud(shapes, frame_num, win):
    if frame_num % 4 == 0:
    #use random number to let the cloud move a bit randomly 
        move(shapes, random.uniform(-1, 2)*8, 0)


#define a test function for animated_cloud
def animate_cloud_test():
    win = gr.GraphWin("cloud", 750, 500)
    cloud = cloud_init(200, 350, 2)
    draw(cloud, win)

    for frame in range(100):
        if win.checkMouse():
            break
        elif win.checkKey == "q":
            break
        else:
            animate_cloud(cloud, frame, win)

            time.sleep(0.1)
            win.update()
    
    win.getMouse()
    win.close()

#define a test function for animated_train
def animate_train_test():
    win = gr.GraphWin("train", 750, 500)
    train = train_init(0, 600, 2.5)
    draw(train, win)

    for frame in range(100):
        if win.checkMouse():
            break
        elif win.checkKey == "q":
            break
        else:
            animate_train(train, frame, win)

            time.sleep(0.1)
            win.update()
    
    win.getMouse()
    win.close()



#define a test function for animated_meadow
def animate_meadow_test():
    win = gr.GraphWin("meadow", 750, 500)
    meadow = meadow_init(100, 400, 3)
    draw(meadow, win)

    for frame in range(100):
        if win.checkMouse():
            break
        elif win.checkKey == "q":
            break
        else:
            animate_meadow(meadow, frame, win)

            time.sleep(0.1)
            win.update()
    
    win.getMouse()
    win.close()


#define a test function for animated_tree
def animate_tree_test():
    win = gr.GraphWin("tree", 750, 500)
    tree = tree_init(200, 500, 1.5)
    draw(tree, win)

    for frame in range(100):
        if win.checkMouse():
            break
        elif win.checkKey == "q":
            break
        else:
            animate_tree(tree, frame, win)

            time.sleep(0.1)
            win.update()
    
    win.getMouse()
    win.close()




if __name__ == "__main__":
    #test every complex element
    test(cloud_init(200, 400, 1.5), cloud_init(400, 350, 1),  "cloud")
    test(house_init(0, 500, 2), house_init(300, 500, 1.5), "house")
    test(rail_init(0, 400, 1.5), rail_init(300, 500, 1),"rail")
    test(train_init(0, 400, 1.5), train_init(200, 300, 1.2), "train")
    test(newvol_init(0, 500, 1.5), newvol_init(200, 700, 1.2), "volcano")
    test(tree_init(0, 500, 1.5), tree_init(400, 500, 1.2), "tree")
    test(meadow_init(240, 500, 1.5), meadow_init(100, 300, 2.5), "meadow")

    #teast every animated function
    animate_cloud_test()
    animate_meadow_test()
    animate_tree_test()
    animate_train_test()


    #execute the main function about the whole scene
    main()

