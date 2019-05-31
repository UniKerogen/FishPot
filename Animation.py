

##############################################################
#   Libraries
##############################################################
import os
import sys
import random
import time


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
TANK_HIGHT = 10
TANK_WIDTH = 15
STEP_SIZE = 9
TANK = [[0 for x in range(TANK_WIDTH*STEP_SIZE)] for y in range(TANK_HEIGHT*STEP)]
TANK_PHASE = [[0 for x in range(TANK_WIDTH)] for y in range(TANK_HEIGHT)]

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
          next_spot[0] = x+1 #Move Right
        else:
          next_spot[1] = y+1 #Move Down
      elif y == TANK_HIGHT-1:
        if chance_move > 1200:
          next_spot[0] = x+1 #Move Right
        else:
          next_spot[1] = y-1 #Move Up
      else:
        if chance_move > 1600:
          next_spot[1] = y-1 #Move Up
        elif chance_move < 800:
          next_spot[0] = y+1 #Move Down
        else:
          next_spot[0] = x+1 #Move Right
    # Right Wall
    elif x == TANK_WIDTH-1:
      if y == 0:
        if chance_move > 1200:
          next_spot[0] = x-1 #Move Left
        else:
          next_spot[1] = y+1 #Move Down
      elif y == TANK_HIGHT-1:
        if chance_move > 1200:
          next_spot[0] = x-1 #Move Left
        else:
          next_spot[1] = y-1 #Move Up
      else:
        if chance_move > 1600:
          next_spot[1] = y-1 #Move Up
        elif chance_move < 800:
          next_spot[0] = y+1 #Move Down
        else:
          next_spot[0] = x-1 #Move Left
    # Middle Section
    else:
      if y == 0:
        if chance_move > 1600:
          next_spot[1] = x+1 #Move Right
        elif chance_move < 800:
          next_spot[0] = y+1 #Move Down
        else:
          next_spot[0] = x-1 #Move Left
      elif y == TANK_HIGHT-1:
        if chance_move > 1600:
          next_spot[1] = y-1 #Move Up
        elif chance_move < 800:
          next_spot[0] = x+1 #Move Right
        else:
          next_spot[0] = x-1 #Move Left
      else:
        if chance_move > 1800:
          next_spot[0] = x-1 #Move Left
        elif chance_move < 600:
          next_spot[1] = y-1 #Move Up
        elif chance_move >= 600 and chance_move < 1200:
          next_spot[0] = x+1 #Move Right
        else:
          next_spot[1] = y+1 #Move Down
  else:
    next_spot = current_spot
  # Next Spot Predicted
  return next_spot
  
  
##############################################################
#   Main Function
##############################################################
def main():
  print("Hello World!")
  
  
##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()
