#Luyi Xiao 
#CS 5001 & 5003
#April 9
import shapes
def drawStack (element, x, y, scale):
    if scale < 20:
        return
        
    element.draw(x, y)

    drawStack( element, x+scale*0.1, y+scale*0.8, 0.8*scale)

    

def main():

    s = shapes.Square( distance=100, color='purple' )
    s.setWidth( 3 )
    s.setStyle( 'jitter' )
    s.setJitter( 3 )

    drawStack( s, -50, -150, 100)

    s.hold()


if __name__ == "__main__":
    main()

    