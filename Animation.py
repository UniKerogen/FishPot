

##############################################################
#   Libraries
##############################################################
import os
import sys
import random
import time
import numpy


##############################################################
#   Pixel Prototype Definition
##############################################################
EMPTY_BLOCK =     [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
EMPTY_BLOCK.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

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
TANK = [[0 for x in range(TANK_WIDTH*STEP_SIZE)] for y in range(TANK_HEIGHT*STEP_SIZE)]
TANK_PHASE = [[0 for x in range(TANK_WIDTH)] for y in range(TANK_HEIGHT)]
BOTTOM_BOUNDARY = ["-" for y in range(TANK_HEIGHT*STEP_SIZE)]


##############################################################
#   Function Prototype
##############################################################
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
                    next_spot[0] = y+1  # Move Down
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
                    next_spot[0] = y+1  # Move Down
                else:
                    next_spot[0] = x-1  # Move Left
        # Middle Section
        else:
            if y == 0:
                if chance_move > 1600:
                    next_spot[1] = x+1  # Move Right
                elif chance_move < 800:
                    next_spot[0] = y+1  # Move Down
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
        else:
            facing = FACE_UP
    else:
        if next_location[0] > current_location[0]:
            facing = FACE_RIGHT
        else:
            facing = FACE_LEFT
    # Return Result Value
    return facing
  
  
def print_tank(fish_location, fish_direction):
    # Clean Tank
    tank = [[0 for x in range(TANK_WIDTH * (STEP_SIZE+1))] for y in range(TANK_HEIGHT * (STEP_SIZE+1))]
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
    # Prepare the Tank
    for x in range(STEP_SIZE):
        for y in range(STEP_SIZE):
            tank[fish_location[0]*STEP_SIZE+x][fish_location[1]*STEP_SIZE+y] = fish_directed[x][y]
    # Print Tank with Boundary
    for y in range(TANK_HEIGHT*STEP_SIZE):
        print("|", TANK[y], "|")
    print(BOTTOM_BOUNDARY)


##############################################################
#   Main Function
##############################################################
def main():
    print("Hello World!")
    # Current Time
    current_location = [random.randint(0, TANK_WIDTH-1), random.randint(0, TANK_HEIGHT-1)]
    print("Current Location :", current_location)
    # Future Time
    next_location = fish_movement(current_location)
    print("Next Location :", next_location)
    fish_direction = fish_face(next_location, current_location)
    # Step into Future
    current_location = next_location
    print_tank(current_location, fish_direction)
    time.sleep(3)
    os.system("clear")
  
  
##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()
