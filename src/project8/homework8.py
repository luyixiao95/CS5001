# CS 5001 Homework 8                                                                                       
# Practice with classes                                                                                    
#                                                                                                          

# model a ball with position, velocity, and acceleration                                                   
class Ball:

    # constructor: position, velocity, and acceleration                                                    
    # each of the values is represented by a 2-element list [x, y]                                         
    def __init__( self, pos, vel, acc ):

        self.pos = pos[:]
        self.vel = vel[:]
        self.acc = acc[:]
        # Q1: why use the slice notation when assigning the fields?                                        

    def getPos( self ):
        return self.pos[:]

    def setPos( self, np ):
        self.pos = np[:]
    
    def getVel( self ):
        return self.vel[:]
    
    def setVel( self, np ):
        self.vel = np[:]
    
    def getAcc( self ):
        return self.acc[:]
    
    def setAcc( self, np):
        self.acc = np[:]
    # Q2: write get and set methods for vel and acc                                                        
    # test your code using function test1                                                                  

    # Q3: using the equation p_new = p_old + dt * vel + 0.5*dt*dt * acc                                    
    # return the new position as a 2-element tuple (parentheses, not square brackets)                      
    # hint: you need to compute the x and y positions separately                                           
    # test your code using function test2                                                                  
    def calcPos( self, dt ):
        p_old = self.getPos()
        vel = self.getVel()
        acc = self.getAcc()
        p_new = []
        for i in range(2):
            p_new_pos = p_old[i]+ dt *vel[i] + 0.5*dt*dt*acc[i]
            p_new.append(p_new_pos)
        p_new = tuple(p_new)
        return p_new

    # Q4: return a list with steps 3-element tuples containing (time, x, y) at intervals of dt                   
    # e.g. if steps is 6 and dt is 0.2, this should return a list of tuples at times 0, 0.2, 0.4, 0.6, 0.8, and 1.0        
    def calcTrajectory( self, dt, steps ):
        trajectory = []
        for t in range(steps):
            time = t * dt
            position = self.calcPos(time)
            traj = (time, position[0], position[1])
            trajectory.append(traj)

        return trajectory    
# test the get/set methods                                                                                 
def test1():

    b = Ball( [0, 1], [3, 5], [0, -10] )
    print( "position should be [0, 1]:       ", b.getPos() )
    print( "velocity should be [3, 5]:       ", b.getVel() )
    print( "acceleration should be [0, -10]: ", b.getAcc() )

# test calcPos                                                                                             
def test2():

    b = Ball( [0, 1], [3, 5], [0, -10] )
    print("position at time 0.0 should be [0.00, 1.00]: [%.2f, %.2f]" % b.calcPos( 0 ) )
    print("position at time 0.2 should be [0.60, 1.80]: [%.2f, %.2f]" % b.calcPos( 0.2 ) )
    print("position at time 0.5 should be [1.50, 2.25]: [%.2f, %.2f]" % b.calcPos( 0.5 ) )
    print("position at time 1.0 should be [3.00, 1.00]: [%.2f, %.2f]" % b.calcPos( 1.0 ) )

# test calcTrajectory                                                                                      
def test3():
    b = Ball( [0, 1], [3, 5], [0, -10] )
    data = b.calcTrajectory( 0.2, 6 )
    print("Time   X     Y")
    for entry in data:
        print("%5.2f %5.2f %5.2f" % entry )

# Q5: write a main function that takes in command line arguments for                                       
# the time step (dt) and the total number of steps and then prints out                                     
# the t, x, y data for a ball with the pos, vel, and acc values                                         
# from the test3 function                                                                                  

if __name__ == "__main__":
    #test1()
    #test2()                                                                           
    test3() # uncomment to run                                                                            
