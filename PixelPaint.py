

##############################################################
#   Libraries
##############################################################
import turtle


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
    

##############################################################
#   Main Function
##############################################################
def main():
    print("Hello World!")
    # Initialize Pen
    myPen = turtle.Turtle()
    myPen.tracer(0)
    myPen.speed(0)
    myPen.color("#000000")
    # Determine Each Box Size
    boxSize = 5
    # Position myPen in top left area of the screen
    myPen.penup()
    myPen.forward(-100)
    myPen.setheading(90)
    myPen.forward(100)
    myPen.setheading(0)
    # Select Paint
    paint = FISH_LEFT
    # Painting
    for i in range (0,len(paint)):
    for j in range (0,len(paint[i])):
		if FISH_LEFT[i][j]==1:
			box(boxSize)
		myPen.penup()
		myPen.forward(boxSize)
		myPen.pendown()	
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(paint[i]))
    myPen.setheading(0)
    myPen.pendown()
    # Update Screen
    myPen.getscreen().update()
    

##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()
