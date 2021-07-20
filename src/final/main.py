#Luyi Xiao
#CS 5001 & CS 5003
#Final, creating a small game - tetris using graphics.py
#main.py
"""In the game, type "a" to let the block move to the left, 
"d" to make the block move to the right,  "w" to make the block rotate 90 degrees and "s" to speed up"""
import frontpage
#main function to encapsulate
def main():
    flag = frontpage.front()
    if flag == True:
        import block2
        block2.rungame()
        
if __name__ == "__main__":
    main()
