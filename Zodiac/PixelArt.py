#Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle

myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")


# This function draws a box by drawing each side of the square and using the fill function
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
	
boxSize = 10	
#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

##Here is an example of how to draw a box	
#box(boxSize)

##Here are some instructions on how to move "myPen" around before drawing a box.
#myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
#myPen.penup()
#myPen.forward(boxSize)
#myPen.pendown()

#Here is how your PixelArt is stored (using a "list of lists")

FISH_LEFT     = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_LEFT.append([0, 0, 0, 1, 0, 0, 0, 1, 0])
FISH_LEFT.append([0, 0, 1, 1, 1, 0, 1, 0, 0])
FISH_LEFT.append([0, 1, 0, 0, 0, 1, 0, 0, 0])
FISH_LEFT.append([0, 0, 1, 1, 1, 0, 1, 0, 0])
FISH_LEFT.append([0, 0, 0, 1, 0, 0, 0, 1, 0])
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
FISH_LEFT.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


for i in range (0,len(FISH_LEFT)):
    for j in range (0,len(FISH_LEFT[i])):
		if FISH_LEFT[i][j]==1:
			box(boxSize)
		myPen.penup()
		myPen.forward(boxSize)
		myPen.pendown()	
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(FISH_LEFT[i]))
    myPen.setheading(0)
    myPen.pendown()
	
myPen.getscreen().update()	
	
