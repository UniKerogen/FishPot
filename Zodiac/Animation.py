##############################################################
#   Libraries
##############################################################
import time
import random
import signal
import os
import turtle as myPen
import sys


##############################################################
#   Pre-Defined Characters
##############################################################
myPen.tracer(0)
myPen.speed('fastest')
myPen.color("#000000")
myPen.hideturtle()


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


FISH_UP =     [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
FISH_UP.append([0, 0, 0, 0, 1, 0, 0, 0, 0])
FISH_UP.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_UP.append([0, 0, 1, 1, 0, 1, 1, 0, 0])
FISH_UP.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_UP.append([0, 0, 0, 0, 1, 0, 0, 0, 0])
FISH_UP.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_UP.append([0, 0, 1, 0, 0, 0, 1, 0, 0])
FISH_UP.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


FISH_DOWN =     [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
FISH_DOWN.append([0, 0, 1, 0, 0, 0, 1, 0, 0])
FISH_DOWN.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_DOWN.append([0, 0, 0, 0, 1, 0, 0, 0, 0])
FISH_DOWN.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_DOWN.append([0, 0, 1, 1, 0, 1, 1, 0, 0])
FISH_DOWN.append([0, 0, 0, 1, 0, 1, 0, 0, 0])
FISH_DOWN.append([0, 0, 0, 0, 1, 0, 0, 0, 0])
FISH_DOWN.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


##############################################################
#   Variable Definition
##############################################################
FACE_LEFT = 10000
FACE_RIGHT = 10001
FACE_UP = 10002
FACE_DOWN = 10003
TANK_HEIGHT = 3
TANK_WIDTH = 6
STEP_SIZE = 9
EMPTY_BOX = [[0 for x in range(STEP_SIZE)] for y in range(STEP_SIZE)]
BOTTOM_BOUNDARY = [1 for x in range(TANK_WIDTH * (STEP_SIZE + 1))]


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

def draw(picture, boxSize, delay):
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
    time.sleep(delay)
    myPen.clear()  # Clear Previous Drawing
    myPen.reset()  # Reset Drawing Position


def fish_movement(current_spot):
    # Update Next Spot of the Fish
    x = current_spot[0]
    y = current_spot[1]
    next_spot = current_spot
    chance_still = random.randint(1, 2400)
    chance_move = random.randint(1, 2400)
    # Location Based Prediction
    if chance_still > 240:
        # Left Wall
        if x == 0:
            if y == 0:
                if chance_move > 1200:
                    next_spot[0] = x+1  # Move Right
                else:
                    next_spot[1] = y+1  # Move Down
            elif y == TANK_HEIGHT-1:
                if chance_move > 1200:
                    next_spot[0] = x+1  # Move Right
                else:
                    next_spot[1] = y-1  # Move Up
            else:
                if chance_move > 1600:
                    next_spot[1] = y-1  # Move Up
                elif chance_move < 800:
                    next_spot[1] = y+1  # Move Down
                else:
                    next_spot[0] = x+1  # Move Right
        # Right Wall
        elif x == TANK_WIDTH-1:
            if y == 0:
                if chance_move > 1200:
                    next_spot[0] = x-1  # Move Left
                else:
                    next_spot[1] = y+1  # Move Down
            elif y == TANK_HEIGHT-1:
                if chance_move > 1200:
                    next_spot[0] = x-1  # Move Left
                else:
                    next_spot[1] = y-1  # Move Up
            else:
                if chance_move > 1600:
                    next_spot[1] = y-1  # Move Up
                elif chance_move < 800:
                    next_spot[1] = y+1  # Move Down
                else:
                    next_spot[0] = x-1  # Move Left
        # Middle Section
        else:
            if y == 0:
                if chance_move > 1600:
                    next_spot[0] = x+1  # Move Right
                elif chance_move < 800:
                    next_spot[1] = y+1  # Move Down
                else:
                    next_spot[0] = x-1  # Move Left
            elif y == TANK_HEIGHT-1:
                if chance_move > 1600:
                    next_spot[1] = y-1  # Move Up
                elif chance_move < 800:
                    next_spot[0] = x+1  # Move Right
                else:
                    next_spot[0] = x-1  # Move Left
            else:
                if chance_move > 1800:
                    next_spot[0] = x-1  # Move Left
                elif chance_move < 600:
                    next_spot[1] = y-1  # Move Up
                elif 600 <= chance_move < 1200:
                    next_spot[0] = x+1  # Move Right
                else:
                    next_spot[1] = y+1  # Move Down
    else:
        next_spot = current_spot
    # Next Spot Predicted
    return next_spot
  

def fish_face(next_location, current_location):
    # Determine where the fish is facing
    if next_location[0] == current_location[0]:
        if next_location[1] > current_location[1]:
            facing = FACE_DOWN
            #print("Facing Down")
        elif next_location[1] < current_location[1]:
            facing = FACE_UP
            #print("Facing Up")
        else:
            facing = FACE_RIGHT
    else:
        if next_location[0] > current_location[0]:
            facing = FACE_RIGHT
            #print("Facing Right")
        else:
            facing = FACE_LEFT
            #print("Facing Left")
    # Return Result Value
    return facing


def getWidth(array):
    for x in range(len(array[0])):
        width = x
    return width


def getHeight(array):
    for y in range(len(array)):
        height = y
    return y


def blank_tank():
    empty_tank = [[0 for x in range(TANK_WIDTH * (STEP_SIZE + 1))] for y in range(TANK_HEIGHT * (STEP_SIZE + 1))]
    return empty_tank


def print_tank(fish_location, fish_direction, delay):
    # Clean Tank
    tank = blank_tank()
    fish_directed = [[0 for x in range(STEP_SIZE)] for y in range(STEP_SIZE)]
    # Select the Correct Fish Location
    if fish_direction == FACE_LEFT:
        fish_directed = FISH_LEFT
    elif fish_direction == FACE_RIGHT:
        fish_directed = FISH_RIGHT
    elif fish_direction == FACE_UP:
        fish_directed = FISH_UP
    elif fish_direction == FACE_DOWN:
        fish_directed = FISH_DOWN
    else:
        print("Fish is right now invisible!")
        fish_directed = EMPTY_BOX
    # Prepare the Tank - Initialize Inner Content
    for x in range(STEP_SIZE):
        for y in range(STEP_SIZE):
            tank[fish_location[1]*STEP_SIZE+y][fish_location[0]*STEP_SIZE+x] = fish_directed[y][x]
    # Prepare the Tank - Add Vertical Boundary
    tankwid = getWidth(tank)
    for y in range(len(tank)):
        tank[y][0] = 1
        tank[y][tankwid] = 1
    # Prepare the Tank - Add Bottom Boundary
    tank.append(BOTTOM_BOUNDARY)
    # Print Tank
    draw(tank, 5, delay)


##############################################################
#   Main Function
##############################################################
def main():
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    # Current Time
    current_location = [random.randint(0, TANK_WIDTH-1), random.randint(0, TANK_HEIGHT-1)]
    while True:
    # Future Time
        present_location = [int(current_location[0]), int(current_location[1])]
        next_location = fish_movement(current_location)
        #print("Next Location :", next_location)
        fish_direction = fish_face(next_location, present_location)
        # Step into Future
        current_location = next_location
        print_tank(current_location, fish_direction, 0.0167)
    myPen.bye()
    #os.system("cls")

##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()
