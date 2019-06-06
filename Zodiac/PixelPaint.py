##############################################################
#   Libraries
##############################################################
import time
import random
import signal
import os
import turtle as myPen


##############################################################
#   Pre-Defined Characters
##############################################################
myPen.tracer(0)
myPen.speed('fastest')
myPen.color("#000000")


##############################################################
#   Pixel Prototype Definition
##############################################################
FISH_LEFT     = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_LEFT.append([0, 0, 0, 1, 0, 0, 0, 1, 0])
FISH_LEFT.append([0, 0, 1, 1, 1, 0, 1, 0, 0])
FISH_LEFT.append([0, 1, 0, 0, 0, 1, 0, 0, 0])
FISH_LEFT.append([0, 0, 1, 1, 1, 0, 1, 0, 0])
FISH_LEFT.append([0, 0, 0, 1, 0, 0, 0, 1, 0])
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

FISH_RIGHT =     [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
FISH_RIGHT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_RIGHT.append([0, 1, 0, 0, 0, 1, 0, 0, 0])
FISH_RIGHT.append([0, 0, 1, 0, 1, 1, 1, 0, 0])
FISH_RIGHT.append([0, 0, 0, 1, 0, 0, 0, 1, 0])
FISH_RIGHT.append([0, 0, 1, 0, 1, 1, 1, 0, 0])
FISH_RIGHT.append([0, 1, 0, 0, 0, 1, 0, 0, 0])
FISH_RIGHT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_RIGHT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


##############################################################
#   Variable Definition
##############################################################
STEP_SIZE = 9
EMPTY_BOX = [[0 for x in range(STEP_SIZE)] for y in range(STEP_SIZE)]

##############################################################
#   Function Prototype
##############################################################
def keyboardInterruptHandler(signal, frame):
        print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
        exit(100)

def box(intDim):
        myPen.begin_fill()
        # 0 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 90 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 180 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 270 deg.
        myPen.forward(intDim)
        myPen.end_fill()
        myPen.setheading(0)

def draw(picture, boxSize):
        myPen.hideturtle()
        myPen.penup()
        myPen.forward(-100)
        myPen.setheading(90)
        myPen.forward(100)
        myPen.setheading(0)

        for i in range (0,len(picture)):
            for j in range (0,len(picture[i])):
                        if picture[i][j]==1:
                                box(boxSize)
                        myPen.penup()
                        myPen.forward(boxSize)
                        myPen.pendown()	
            myPen.setheading(270) 
            myPen.penup()
            myPen.forward(boxSize)
            myPen.setheading(180) 
            myPen.forward(boxSize*len(picture[i]))
            myPen.setheading(0)
            myPen.pendown()

        myPen.getscreen().update()
        time.sleep(3)  # Sleep for 3 seconds
        myPen.clear()  # Clear Previous Drawing
        myPen.reset()  # Reset Drawing Position

        
##############################################################
#   Main Function
##############################################################
def main():
        signal.signal(signal.SIGINT, keyboardInterruptHandler)
        
        while True:
                print("A Random Number ->", random.randint(1,1000))
                ctime = time.localtime(time.time())
                print("Current Time ->", ctime.tm_hour, ":", ctime.tm_min, ":", ctime.tm_sec)
                time.sleep(1)

                boxSize = 10
                if random.randint(1,2) == 1:
                    draw(FISH_LEFT, boxSize)
                else:
                    draw(FISH_RIGHT, boxSize)
                os.system("cls")

                
##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
        main()
