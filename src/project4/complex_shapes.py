#Luyi Xiao
#CS 5001 & 5003
#Feb 13, 2020 complex_shape.py
#Build a new scene using graphicPlus:

import graphicsPlus as gr

#design several basic elements as list

#Volcano list, that is object1
def volcano_init(x, y, scale):

    #draw the root of the volcano firstly
    vol_root_list =[gr.Point(x+101*scale, y+519*scale), gr.Point(x+123*scale, y+482*scale),
    gr.Point(x+155*scale, y+407.5*scale), gr.Point(x+161*scale, y+391*scale),   #from 161,391
    gr.Point(x+170.5*scale, y+364.5*scale), gr.Point(x+176*scale, y+344*scale),
    gr.Point(x+187.5*scale, y+338*scale), gr.Point(x+196.5*scale, y+338.5*scale),
    gr.Point(x+212*scale, y+346*scale), gr.Point(x+219*scale, y+345*scale),
    gr.Point(x+229*scale, y+342*scale), gr.Point(x+242*scale, y+335.5*scale),
    gr.Point(x+249*scale, y+341*scale), gr.Point(x+260*scale, y+369*scale), #to 260,369 still need to used in the lava list
    gr.Point(x+286.5*scale, y+426*scale), gr.Point(x+302.5*scale, y+453*scale),
    gr.Point(x+332.5*scale, y+500*scale) ]

    vol_root = gr.Polygon(vol_root_list)
    vol_root.setFill(gr.color_rgb(205, 188, 114 ))
    vol_root.setOutline(gr.color_rgb(87, 71, 54))
    vol_root.setWidth(5)


    #draw the magma within the crater
    magma_init_list1=[gr.Point(x+161*scale, y+391*scale),
    gr.Point(x+170.5*scale, y+364.5*scale), gr.Point(x+176*scale, y+344*scale),
    gr.Point(x+187.5*scale, y+338*scale), gr.Point(x+196.5*scale, y+338.5*scale),
    gr.Point(x+212*scale, y+346*scale), gr.Point(x+219*scale, y+345*scale),
    gr.Point(x+229*scale, y+342*scale), gr.Point(x+242*scale, y+335.5*scale),
    gr.Point(x+249*scale, y+341*scale), gr.Point(x+260*scale, y+369*scale),
    gr.Point(x+256*scale, y+374*scale), gr.Point(x+252*scale, y+373.5*scale),
    gr.Point(x+250.5*scale, y+379.5*scale), gr.Point(x+255.5*scale, y+395.5*scale),
    gr.Point(x+262*scale, y+420.5*scale), gr.Point(x+261*scale, y+427*scale),
    gr.Point(x+256.5*scale, y+426.5*scale), gr.Point(x+246*scale, y+403.5*scale),
    gr.Point(x+240*scale, y+369.5*scale), gr.Point(x+232*scale, y+364*scale),
    gr.Point(x+223*scale, y+368.5*scale), gr.Point(x+214.5*scale, y+383.5*scale),
    gr.Point(x+208.5*scale, y+386.5*scale), gr.Point(x+202*scale, y+382*scale),
    gr.Point(x+197.5*scale, y+372.5*scale), gr.Point(x+192.5*scale, y+369.5*scale),
    gr.Point(x+187.5*scale, y+370.5*scale), gr.Point(x+168*scale, y+387*scale)]

    magma1 = gr.Polygon(magma_init_list1)
    magma1.setFill(gr.color_rgb(232, 166, 153))  
    magma1.setOutline(gr.color_rgb(87, 71, 54))
    magma1.setWidth(3)

    #draw the magma that burst out of the crator
    magma_init_list2=[gr.Point(x+187.5*scale, y+338*scale), gr.Point(x+196.5*scale, y+338.5*scale),
    gr.Point(x+212*scale, y+346*scale), gr.Point(x+219*scale, y+345*scale),
    gr.Point(x+229*scale, y+342*scale), gr.Point(x+237.5*scale, y+337*scale),
    gr.Point(x+237*scale, y+326*scale), gr.Point(x+239.5*scale, y+315*scale),
    gr.Point(x+245*scale, y+300.5*scale), gr.Point(x+259*scale, y+284*scale),
    gr.Point(x+162.5*scale, y+286*scale), gr.Point(x+170*scale, y+295*scale),
    gr.Point(x+179.5*scale, y+308.5*scale), gr.Point(x+186*scale, y+322*scale)]

    magma2 = gr.Polygon(magma_init_list2)
    magma2.setFill(gr.color_rgb(232, 166, 153))
    volcano = [vol_root, magma1, magma2]
    return volcano



#Draw an island float above the magma and there are buildings on it, that is object 2.
def island_init(x, y, scale):
    #draw the island firstly
    island_list = [gr.Point(x+75.5*scale, y+180*scale), gr.Point(x+105*scale, y+160*scale),
    gr.Point(x+323*scale, y+160*scale), gr.Point(x+221*scale, y+230*scale),
    gr.Point(x+189.5*scale, y+233*scale), gr.Point(x+101.5*scale, y+201*scale)]

    is_base = gr.Polygon(island_list)
    is_base.setFill(gr.color_rgb(204, 204, 204))
    is_base.setOutline("navy")
    is_base.setWidth( 5 )

    #draw several buildings above the island
    bu1 = gr.Rectangle(gr.Point(x+151*scale, y+160*scale), gr.Point(x+167*scale, y+76*scale))
    bu1.setFill("green")
    bu2 = gr.Rectangle(gr.Point(x+167*scale, y+160*scale), gr.Point(x+189*scale, y+68*scale))
    bu2.setFill("gold")
    bu3 = gr.Rectangle(gr.Point(x+189*scale, y+160*scale), gr.Point(x+210*scale, y+64*scale))
    bu3.setFill("peru")
    bu4 = gr.Rectangle(gr.Point(x+210*scale, y+160*scale), gr.Point(x+230*scale, y+84*scale))
    bu4.setFill("orchid")

    island = [is_base, bu1, bu2, bu3, bu4]
    return island


#draw part of the scene in the artwork La Era by Diego Rivera

def LaEra_init(x, y, scale):
    #draw the wall first

    wall1=gr.Rectangle(gr.Point(x+0*scale, y+220*scale), gr.Point(x+180*scale, y+240*scale))
    wall1.setFill(gr.color_rgb(179, 136, 91))

    wall2=gr.Rectangle(gr.Point(x+0*scale, y+240*scale), gr.Point(x+180*scale, y+255*scale))
    wall2.setFill(gr.color_rgb(142, 40, 26))

    wall3=gr.Rectangle(gr.Point(x+270*scale, y+220*scale), gr.Point(x+450*scale, y+240*scale))
    wall3.setFill(gr.color_rgb(179, 136, 91))

    wall4=gr.Rectangle(gr.Point(x+270*scale, y+240*scale), gr.Point(x+450*scale, y+255*scale))
    wall4.setFill(gr.color_rgb(142, 40, 26))

    #draw the door of the pic
    door_list = [gr.Point(x+180*scale, y+255*scale), gr.Point(x+180*scale, y+180*scale),
    gr.Point(x+270*scale, y+180*scale), gr.Point(x+270*scale, y+255*scale)
    ]
    door = gr.Polygon(door_list)
    door.setFill("silver")


    #Draw the roof of the door

    roof_list = [gr.Point(x+175*scale, y+183*scale), gr.Point(x+185*scale, y+148*scale),
    gr.Point(x+265*scale, y+148*scale), gr.Point(x+274*scale, y+183*scale)
    ]
    roof = gr.Polygon(roof_list)
    roof.setFill(gr.color_rgb(37, 29, 27))

    #Draw a horse finally

    horse_list = [ gr.Point(x+196.5*scale, y+400*scale), gr.Point(x+197.5*scale, y+356.5*scale),
    gr.Point(x+199*scale, y+349*scale), gr.Point(x+198.5*scale, y+341*scale),
    gr.Point(x+199.5*scale, y+349*scale), gr.Point(x+199*scale, y+331.5*scale),
    gr.Point(x+200.7*scale, y+327.8*scale), gr.Point(x+204.4*scale, y+318*scale),
    gr.Point(x+208.7*scale, y+314.6*scale), gr.Point(x+214.4*scale, y+311*scale),
    gr.Point(x+220.8*scale, y+310.4*scale), gr.Point(x+240.6*scale, y+330.6*scale),
    gr.Point(x+242.8*scale, y+308.8*scale), gr.Point(x+246.4*scale, y+302.9*scale),
    gr.Point(x+250*scale, y+297.8*scale), gr.Point(x+252*scale, y+295.3*scale),
    gr.Point(x+250.7*scale, y+297.4*scale), gr.Point(x+249.3*scale, y+292.7*scale),
    gr.Point(x+248.6*scale, y+289.3*scale), gr.Point(x+251.4*scale, y+291.8*scale),
    gr.Point(x+253.5*scale, y+293.6*scale), gr.Point(x+257*scale, y+292*scale),
    gr.Point(x+260.6*scale, y+292.8*scale), gr.Point(x+263.5*scale, y+289.4*scale),
    gr.Point(x+266.3*scale, y+287.7*scale), gr.Point(x+265.6*scale, y+291.1*scale),
    gr.Point(x+263.4*scale, y+296.2*scale), gr.Point(x+264.8*scale, y+301.2*scale),
    gr.Point(x+264.8*scale, y+303.7*scale), gr.Point(x+264*scale, y+307.1*scale),
    gr.Point(x+263.3*scale, y+312.2*scale), gr.Point(x+262.5*scale, y+319*scale),
    gr.Point(x+262.5*scale, y+323.2*scale), gr.Point(x+260.3*scale, y+326.6*scale),
    gr.Point(x+258.9*scale, y+325.7*scale), gr.Point(x+256.1*scale, y+319.8*scale),
    gr.Point(x+254.7*scale, y+319.8*scale), gr.Point(x+251.1*scale, y+327.4*scale),
    gr.Point(x+252.4*scale, y+337.6*scale), gr.Point(x+251.7*scale, y+344.3*scale),
    gr.Point(x+246.6*scale, y+353.6*scale), gr.Point(x+243.7*scale, y+367.1*scale),
    gr.Point(x+242.2*scale, y+377.3*scale), gr.Point(x+241.3*scale, y+396*scale),
    gr.Point(x+243.4*scale, y+398.4*scale), gr.Point(x+242.7*scale, y+399.3*scale),
    gr.Point(x+239.1*scale, y+399.3*scale), gr.Point(x+237*scale, y+397.6*scale),
    gr.Point(x+238.6*scale, y+385.7*scale), gr.Point(x+238.6*scale, y+372.2*scale),
    gr.Point(x+239.5*scale, y+357.8*scale), gr.Point(x+238.1*scale, y+357*scale),
    gr.Point(x+234.5*scale, y+358.7*scale), gr.Point(x+233.8*scale, y+363.7*scale),
    gr.Point(x+232.3*scale, y+369.7*scale), gr.Point(x+233*scale, y+373.9*scale),
    gr.Point(x+230.8*scale, y+379*scale), gr.Point(x+230*scale, y+386.5*scale),
    gr.Point(x+232.1*scale, y+392.5*scale), gr.Point(x+234.2*scale, y+395.9*scale),
    gr.Point(x+234.2*scale, y+396.7*scale), gr.Point(x+232.8*scale, y+397.6*scale),
    gr.Point(x+227.8*scale, y+395.9*scale), gr.Point(x+227.2*scale, y+385.7*scale),
    gr.Point(x+228*scale, y+378.1*scale), gr.Point(x+226.6*scale, y+374.7*scale),
    gr.Point(x+228.8*scale, y+367.1*scale), gr.Point(x+229.5*scale, y+360.3*scale),
    gr.Point(x+220.3*scale, y+360.3*scale), gr.Point(x+218.1*scale, y+370.4*scale),
    gr.Point(x+213.8*scale, y+379.8*scale), gr.Point(x+213.7*scale, y+389.9*scale),
    gr.Point(x+215.8*scale, y+395.8*scale), gr.Point(x+221.4*scale, y+406.8*scale),
    gr.Point(x+220.6*scale, y+407.7*scale), gr.Point(x+214.3*scale, y+404.3*scale),
    gr.Point(x+207.4*scale, y+379.7*scale), gr.Point(x+208.2*scale, y+375.5*scale),
    gr.Point(x+209.6*scale, y+371.3*scale), gr.Point(x+209.7*scale, y+362*scale),
    gr.Point(x+208.9*scale, y+356*scale), gr.Point(x+206.1*scale, y+363.8*scale),
    gr.Point(x+201.8*scale, y+367*scale), gr.Point(x+200.2*scale, y+389*scale),
    gr.Point(x+200.1*scale, y+400*scale) ]
    
    horse = gr.Polygon(horse_list)
    horse.setFill(gr.color_rgb(80, 29, 28))

    LaEra = [wall1, wall2, wall3, wall4, door, roof, horse]
    return LaEra

#define the draw function to simplify the main function below
def draw(list, win):
    for item in list:
        item.draw(win)


#define three test functions
def test1():  #test for volcano_init function and draw two volcanoes with two different scales and places
    win = gr.GraphWin("Volcano", 600, 600)
    scene = volcano_init(0, 0, 1) + volcano_init(400,200, 0.5) #combine two lists together
    draw(scene, win)
    win.getMouse()
    win.close()
 
def test2(): #test to draw two islands with different scales and places
    win = gr.GraphWin("island", 600, 600)
    scene = island_init(0, 0, 1) + island_init(200, 200, 0.5)
    draw(scene, win)
    win.getMouse()
    win.close()

def test3(): #test to draw two scenes from the artwork LaEra with different scales and places
    win = gr.GraphWin("LaEra", 600, 600)
    scene = LaEra_init(0, 0, 1)+ LaEra_init(200, 200, 0.5)
    draw(scene, win)
    win.getMouse()
    win.close()




###################################################
###################################################
#define some new objects in project 5:

#define a house function, contains house_base, window, door, knob, chimney, roof, gas1, gas2, gas3
def house_init(x, y, scale):
    #house_base
    house_base = gr.Rectangle(gr.Point(x+0*scale, y-0*scale), gr.Point(x+40*scale, y-40*scale))
    house_base.setFill(gr.color_rgb(255, 204, 50))

    #window
    window = gr.Rectangle(gr.Point(x+5*scale, y-20*scale), gr.Point(x+15*scale, y-28*scale)
    window.setFill(gr.color_rgb(255, 102, 153))

    #door
    door = gr.Rectangle(gr.Point(x+29*scale, y-0*scale), gr.Point(x+38*scale, y-16*scale))
    door.setFill(gr.color_rgb(255, 153, 102))

    #knob
    knob = gr.Circle(gr.Point(x+30*scale, y-8*scale), 1*scale)
    knob.setFill(gr.color_rgb(153, 255, 255) 
    #chimney
    chimney = gr.Rectangle(gr.Point(x+26*scale, x-53*scale), gr.Point(x+28*scale, x-47*scale))
    chimney.setFill(gr.color_rgb(102, 153, 255))

    #roof
    roof_list = [gr.Point(x+0*scale, y-40*scale), gr.Point(x+20*scale, y-55*scale), gr.Point(x+40*scale, y-40*scale)]\
    roof = gr.Polygon(roof_list)
    roof.setFill(gr.color_rgb(255, 255, 102))
    
    #tho oval gases
    gas1 = gr.Oval(gr.Point(x+26*scale, y-54*scale), gr.Point(x+28*scale, y-52*scale))
    gas2 = gr.Oval(gr.Point(x+25*scale, y-48*scale), gr.Point(x+29*scale, y-50)
    gas1.setFill("gray")
    gas2.setFill("gray")


    house = [house_base, window, door, knob, chimney, roof, gas1, gas2]
    return house

def test4(x, y, scale):
    win = gr.GraphWin("House", 500, 500)
    house1 = house_init(0, 0, 1)
    draw(house1)
    win.getMouse()
    win.close()


test4(0, 0, 1)



