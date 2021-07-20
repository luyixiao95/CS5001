#Luyi Xiao
#CS 5001 & CS 5003
#Final, creating a small game - tetris using graphics.py

import random
import graphicsPlus as gr
import time

win = gr.GraphWin("Tetris", 700, 800, False)
canvas = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 800))
canvas.draw(win)
#The list instant_block will store all coordinates of every block in the window instantly
instant_block = []

#The list active_object will create all the square objects
active_object = []

#7 lists to contain different angle of 7 types of blocks
#Use these lists in the spinning part
O_shape = [[[0, 0], [0, 1], [1, 0], [1, 1]]]
I_shape = [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]] 
J_shape = [[[0, 0], [0, 1], [1, 1], [2, 1]], [[0, 2], [1, 0], [1, 1], [1, 2]], [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [0, 1], [0, 2], [1, 0]]]
L_shape = [[[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 0], [2, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]]]
T_shape = [[[0, 1], [1, 0], [1, 1], [2, 1]], [[0, 1], [1, 0], [1, 1], [1, 2]], [[0, 0], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 1]]]
Z_shape = [[[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0], [1, 1]]]
S_shape = [[[0, 1], [1, 0], [1, 1], [2, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]]]

all_shapes =[O_shape, I_shape, J_shape, L_shape, T_shape, Z_shape, S_shape]

score = 0
hs = open("HighestScore.txt", "r")
Highestscore = int(hs.read())

#score board
def scorescreen(score):
    screen = gr.Rectangle(gr.Point(450, 300), gr.Point(650, 400))
    screen.setFill("dimgray")
    screen.draw(win)

    title = gr.Text(gr.Point(550, 260), "score board")
    title.setFace("arial")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)

    score_num = gr.Text(gr.Point(550, 350), score)
    score_num.setTextColor("red")
    score_num.setFace("courier")
    score_num.setSize(23)
    score_num.setStyle("bold")
    score_num.draw(win)

#Create a new class Block to draw a block shape contains 4 basic squares, with random color
class Block:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.block_pos_list = [] #Elements in the list are coordinates of four squares in this class
        self.shape_list = []   #Elements in this list contain four square objects
        self.type = None #the type of the block, will be refreshed when using classification method
        self.num = None #the num of the block, will be refreshed when using classification method
    
    def tetris(self, col, row = -3):
        """Use recursion to create the four-square block which is the basic element of the game
        Randomly pick one sub-sub-list from the all_shapes list might be an easier way to do so 
        but as the project has this request on doing resursion part, I chose this way instead."""

        #When there are four squares in the shape, stop the recursion
        if len(self.block_pos_list) > 3:

            return self.block_pos_list
        
        #Set a new position that might be the place of a square 
        potential_pos = [col, row]
        #Append the position to the list
        if potential_pos not in self.block_pos_list:
            if self.block_pos_list == []:
                self.block_pos_list.append(potential_pos)
            else:
                """sort the position sublists in order
                Writing this part of codes is ahead of the class, so my sort way is very weird.
                Yet I still saved this part as I think at least it is useful"""
                index = 0
                for pos_list in self.block_pos_list:
                    if potential_pos[0] > pos_list[0]: 
                        index += 1
                    elif potential_pos[0] == pos_list[0]:
                        if potential_pos[1] > pos_list[1]:
                            index += 1

                self.block_pos_list.insert(index, potential_pos)
                
        #Randomly set the next col and row of the block
        dice = random.random()
        if dice < 0.3 and col - 1 > 0:
            col = col - 1
        elif dice >= 0.3 and dice < 0.6 and row - 1 > 0:
            row = row - 1
        elif dice >= 0.6 and dice <0.8:
            col = col + 1
        elif dice >=0.8:
            row = row + 1
        self.tetris(col, row)

    #the classification method is to distinguish the blocks in the block_pos_list with the given all_shape list
    def classification(self):
        st_pos_list = []
        #The coordinates of the block might be different from the standard one stored in the all_shape list
        #Therefore it is necessary to revise the coordinaates as the very standard version 
        bpl = self.block_pos_list
        #Get the min col and row value of the block
        colmin = bpl[0][0]
        rowmin = min(bpl[0][1], bpl[1][1], bpl[2][1], bpl[3][1])  
        for position in bpl:
            #In the standard block, the min value of the col and row are all 0
            #So every col and row was subtract colmin and rowmin value to standarize the block coordinate
            st_col = position[0]-colmin
            st_row = position[1]-rowmin
            st_pos = [st_col, st_row]
            st_pos_list.append(st_pos)

        #compare the standard positon of this block to the standard one and get the type and num of the block
        #This will be useful when rotate the block
        for indexa in range(7):
            length = len(all_shapes[indexa])
            for indexb in range(length):
                if all_shapes[indexa][indexb] == st_pos_list:
                    self.type = indexa
                    self.num = indexb


    #draw method to draw the block in a given block_pos_list, also return a shape_list with four square objects created inside
    def draw(self):
        for element in self.block_pos_list:
            xpo = element[0] * 40
            ypo = element[1] * 40
            square = gr.Rectangle(gr.Point(xpo, ypo), gr.Point(xpo + 40, ypo + 40))
            square.setFill(gr.color_rgb(self.color[0], self.color[1], self.color[2]))
            self.shape_list.append(square)
            square.draw(win)
    
    #move method to move the square objects
    def move(self, dx, dy):
        for element in self.shape_list:
            element.move(dx, dy)

    #define a spin method to revolve the block with 90 degree counterclockwise
    """It is a little bit hard to do the spinning not only because there is no rotation methods in the zelle graphics
    but also the rotation of tetris shapes is not pinned on one point, it contains translation. 
    Therefore, I listed all the possible rotation shapes in all_shapes, and once the command "rotate" was set,
    just replace the next shape element in the sublist and move the squares to the right place"""
    def spin(self):
        newnum = None
    
        former_blocks = all_shapes[self.type][self.num]
        pos_change = []
        if self.num + 1 < len(all_shapes[self.type]):
            latter_blocks = all_shapes[self.type][self.num + 1]
            newnum = self.num + 1
        else:
            #if the block is the last positon of the list, the next one will be the first element of the list
            latter_blocks = all_shapes[self.type][0]
            newnum = 0

        for i in range(4):
            coli = former_blocks[i][0]
            rowi = former_blocks[i][1]
            colf = latter_blocks[i][0]
            rowf = latter_blocks[i][1]
            d_col = colf - coli
            d_row = rowf - rowi
            d_pos = [d_col, d_row]
            pos_change.append(d_pos)


        return pos_change, newnum, latter_blocks
        

    def getBlockPosList(self):
        return self.block_pos_list


    
#draw one set of squares as a block, the speed is faster as the game continues
def singleBlock(col, row = -3):
    a = Block()
    a.tetris(col, row)
    a.draw()
    return a

#arrange function aims to add the coordinates of four squares to the instant_block list and 4 objects to the active_object list
def arrange(a):
    BlockPosList = a.block_pos_list
    for element in BlockPosList:
        instant_block.append(element)
    a.classification()
    for object in a.shape_list:
        active_object.append(object)


def fall(a, speed):
    #A flag to control if the block is falling down instantly or slowly
    directly_end = False

    for frame in range(100):
        local_frequence = 1
        for point in range(-4, 0):
            col = instant_block[point][0]
            row = instant_block[point][1]
            #if the block is attach to the squares below, this block stops falling down
            for sublist in instant_block[0:-4]:
                if sublist[0] == col and sublist[1] - 1 == row:
                    return


        for point in range(-4, 0):
            instant_block[point][1] += 0.25
        
        #when type "d" key, the block moves right
        key = win.checkKey()

        
        #When type "a" key, the block moves left 
        if key == "Left":
            flag = True
            for newpos in instant_block[-4:]:
                newcol = newpos[0]
                newrow = newpos[1]
                for oldpos in instant_block[:-4]:
                    oldcol = oldpos[0]
                    oldrow = oldpos[1]

                    #in case the block position after moving will overlap with the existing blocks, the flag is assigned to false
                    if  (newcol == oldcol + 1 and int(newrow) == int(oldrow)) or (newcol == oldcol + 1 and int(newrow) == int(oldrow)-1):
                        flag = False
            
            test_list = [instant_block[i][0]>0 for i in range(-4, 0)]
            #Avoid the situation which after moving, the shape is out of range
            if test_list != [True, True, True, True]:
                flag = False
        
            #only when there are no risks after moving, the block can actually move 
            if flag == True:
                a.move(-40, 0)
                for point in range(-4, 0):
                    instant_block[point][0] -=1
        
        elif key == "Right":
            flag = True
            for newpos in instant_block[-4:]:
                newcol = newpos[0]
                newrow = newpos[1]
                for oldpos in instant_block[:-4]:
                    oldcol = oldpos[0]
                    oldrow = oldpos[1]

                    if  (newcol == oldcol - 1 and int(newrow) == int(oldrow)) or (newcol == oldcol - 1 and int(newrow) == int(oldrow)-1):
                        flag = False
            
            test_list = [instant_block[i][0]<9 for i in range(-4, 0)]
            if test_list != [True, True, True, True]:
                flag = False
        
            if flag == True:
                a.move(40, 0)
                for point in range(-4, 0):
                    instant_block[point][0] +=1



        #when type "w" key, the block spins
        elif key == "Up":
            pos_change, newnum, latter_blocks = a.spin()
            flag = True
            newposlist = []
            for point in range(-4, 0):
                index = point + 4
                #the col and row after spinning
                newcol = instant_block[point][0] + pos_change[index][0]
                newrow = instant_block[point][1] + pos_change[index][1]
                newpos = [newcol, newrow]
                newposlist.append(newpos)
                #test if the potential position after spinning overlaps with the existing squares
                #if so, False value is assigned to flag
                for sublist in instant_block[:-4]:
                    if (sublist[0] == newpos[0] and int(sublist[1]) == int(newpos[1])) or (sublist[0] == newpos[0] and int(sublist[1]) == int(newpos[1]+1)) :
                        flag = False
                #the new col and row must be in the range of the win
                if newcol > 9 or newcol < 0 or newrow >19 or newcol < 0:
                    flag = False
            
            
            if flag == True:
                #when spinning the block, the corresponding field of the object should be refreshed
                a.num = newnum
                a.block_pos_list = latter_blocks
                for index in range(4):
                    point = index - 4
                    #move the squares to the new, spinning position
                    active_object[point].move(pos_change[index][0]*40, pos_change[index][1]*40)
                    
                    #update the newest coordinations
                    instant_block[point][0] = newposlist[index][0]
                    instant_block[point][1] = newposlist[index][1]



        #when type "s" key, the block falling down faster
        elif key == "Down":
            local_frequence = 0.01
        #type blank space to directly falling down till the bottom site
        elif key == "space":
            directly_end = True


        a.move(0, 10)

        if directly_end == True:
            time.sleep(0)

        else:
            time.sleep((0.08 - speed*0.003)*local_frequence)
        win.update()

        for pos in instant_block[-4:]:
            if pos[1] >= 19:
                return
#check if one row is filled up with the squares. If so, cut the whole row off.
def check():
    addscore = 0
    for add_position in instant_block[-4:]:
        add_row = add_position[1]
        index = 0
        index_list = []
        ori_col_list = []
        
        for ori_position in instant_block:
            
            ori_row = ori_position[1]
            if ori_row == add_row:
                ori_col = ori_position[0]
                ori_col_list.append(ori_col)
                index_list.append(index)

            index += 1

        ori_col_list.sort()

        if ori_col_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
            addscore += 100
            index_list.sort(reverse=True)
            for index in index_list:
                active_object.pop(index).undraw()
                instant_block.pop(index)
                

            index2 = 0

            #move the squares ahead of the removal row
            for pos in instant_block:
                if pos[1] < add_row:
                    pos[1] += 1
                    active_object[index2].move(0, 40)
                

                index2 += 1
    return addscore
    
#test if the game is over            
def Gameover():
    for square in active_object:
        square.undraw()
    text = gr.Text(gr.Point(200, 400), "Game Over!" + "\n" +"Your score is " + str(score))
    text.setFace("arial")
    text.setStyle("bold")
    text.setSize(20)
    text.draw(win)

    if score > Highestscore:
        text2 = gr.Text(gr.Point(200, 500), "You break the record!")
        text2.setFace("arial")
        text2.setStyle("bold")
        text2.setSize(20)
        text2.draw(win)

        hs = open("HighestScore.txt", "w")
        hs.write(str(score))

#Run the game use the following function
def rungame():
    global score

    for i in range(100):
        scorescreen(score)
        a = singleBlock(3)
        arrange(a)
        fall(a, i)
        print(instant_block)
        addscore = check()
        score += addscore
        for point in instant_block[-4:]:
            if point[1] < 0:
                Gameover()
                win.getMouse()
                win.close()

    
