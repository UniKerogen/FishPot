
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
TANK_HEIGHT = 7
TANK_WIDTH = 10
STEP_SIZE = 9
EMPTY_BOX = [[0 for x in range(STEP_SIZE)] for y in range(STEP_SIZE)]
BOTTOM_BOUNDARY = [1 for x in range(TANK_WIDTH * (STEP_SIZE + 1))]


HEALTH_MAX = 100.0
WATER_MAX = 120.0
FOOD_MAX = 200.0
WATER_UPPER_THRESHOLD = 94
WATER_LOWER__THRESHOLD = 85
FOOD_UPPER_LIMIT = 110
FOOD_MID_POINT = 100
FOOD_LOW_LIMIT = 90


##############################################################
#   Function Prototype
##############################################################
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Stopping...".format(signal))
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
    # Setup Drawing Parameter
    myPen.tracer(0)
    myPen.speed('fastest')
    myPen.color("#000000")
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
    # Update Drawing Screen
    myPen.getscreen().update()
    time.sleep(delay) # System Time Delay
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
        elif next_location[1] < current_location[1]:
            facing = FACE_UP
        else:
            facing = FACE_RIGHT
    else:
        if next_location[0] > current_location[0]:
            facing = FACE_RIGHT
        else:
            facing = FACE_LEFT
    # Return Result Value
    return facing


def getWidth(array):
    # Get width of an array
    for x in range(len(array[0])):
        width = x
    return width


def getHeight(array):
    # Get height of an array
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


def health_calculation( health, water, food ):
    multiplier = 0.1
    # Food Composition
    if food > FOOD_UPPER_LIMIT:
        foodc = (FOOD_UPPER_LIMIT - food) / FOOD_UPPER_LIMIT * multiplier
    elif food < FOOD_LOW_LIMIT:
        foodc = (food - FOOD_LOW_LIMIT) / FOOD_LOW_LIMIT * multiplier
    else:
        foodc = abs(food - FOOD_MID_POINT) / FOOD_MID_POINT * multiplier
    # Water Composition
    if water < WATER_UPPER_THRESHOLD:
        waterc = (water - WATER_LOWER__THRESHOLD) / WATER_LOWER__THRESHOLD * multiplier
    else:
        waterc = (WATER_UPPER_THRESHOLD - WATER_LOWER__THRESHOLD) / WATER_LOWER__THRESHOLD * multiplier
    # Health Calculation
    heathc = health * (1 + foodc + waterc)
    if heathc > HEALTH_MAX:
        heathc = HEALTH_MAX
    # Return Value
    return heathc


def feed(food, water, info):
    # Chance of Food Release
    chance_food = random.randint(1, 1000)
    if chance_food < 650:
        food_release = 1
    else:
        food_release = 0
    # Chance of Food Visibility
    chance_water = random.randint(1, 1000)
    if water > WATER_UPPER_THRESHOLD:
        if chance_water < 750:
            food_recognition = 1
        else:
            food_recognition = 0
    else:
        if chance_water < 450:
            food_recognition = 1
        else:
            food_recognition = 0
    # Chance of Digest
    chance_digest = 10 * random.randint(1, 1000) / 1000
    # Result food
    if food_release + food_recognition == 2:
        foodr = food + chance_digest
        print("Fed with amount ", chance_digest)
    else:
        foodr = food
        print("The food is ignored")
    # Result food - Determine Max
    if foodr > FOOD_MAX:
        foodr = FOOD_MAX
    # Result fodd - Save to info
    info[6] = foodr


def consumed(hour, info):
    # Consumption per hour
    for x in range (hour):
        info[5] = info[5] * (0.9995 - abs(info[6]-100)/100 * 0.0001)
        info[6] = info[6] * 0.992
    return info


def check_save_file():
    # Check for save file and load info
    # Check for existence
    exists = os.path.isfile('data')
    # Check for empty file
    if exists:
        not_empty = os.stat('data').st_size
    else:
        not_empty = 0
    current_time = time.localtime(time.time())
    # Load from Save
    if exists and not_empty != 0:
        f = open('data', 'r')
        time_year = int(f.readline().strip())
        time_month = int(f.readline().strip())
        time_date = int(f.readline().strip())
        time_hour = int(f.readline().strip())
        health = float(f.readline().strip())
        water = float(f.readline().strip())
        food = float(f.readline().strip())
        f.close()
    # Establish New Save
    else:
        time_year = current_time.tm_year
        time_month = current_time.tm_mon
        time_date = current_time.tm_mday
        time_hour = current_time.tm_hour
        health = HEALTH_MAX
        water = WATER_MAX
        food = FOOD_MAX / 2
    # Combine Information
    info = [time_year, time_month, time_date, time_hour, health, water, food]
    # Calculate Time Passed
    if exists:
        pass_year = current_time.tm_year - info[0]
        pass_month = current_time.tm_mon - info[1]
        pass_day = current_time.tm_mday - info[2]
        pass_hour = current_time.tm_hour - info[3]
        # Calculate Total Hour Pass
        hour = pass_hour + 24*(pass_day + 30*(pass_month + 12*pass_year))
        consumed(hour, info)
        # Update Information
        info[0] = current_time.tm_year
        info[1] = current_time.tm_mon
        info[2] = current_time.tm_mday
        info[3] = current_time.tm_hour
    # Return Information
    return info


def save_file(info):
    # Save Current Status
    f = open('data', 'w')
    f.write(str(info[0]), '\n')
    f.write(str(info[1]), '\n')
    f.write(str(info[2]), '\n')
    f.write(str(info[3]), '\n')
    f.write(str(info[4]), '\n')
    f.write(str(info[5]), '\n')
    f.write(str(info[6]), '\n')
    f.close()


def delete_save():
    # Delete Previous Save
    f = open('data', 'w')
    f.close()
    print("File Deleted. Please Restart")


def print_status(info):
    # Print Current Pot Status
    print("Current Health : ", info[4])
    print("Current Water : ", info[5])
    print("Current Food : ", info[6])


def print_menu():
    # Print Menu
    print("###### FishPot Simulator ######")
    print("Menu:")
    print("1. Print Current Status")
    print("2. Change Water")
    print("3. Feed")
    print("4. Save & Exit")
    print("5. Exit without Save")
    print("6. Delete Current Save")
    print("7. Fast Forward an Hour")
    print("8. Show Tank for 10 seconds")


def forward(hour):
    # Forward hour by 1
    hour = hour - 1
    return hour


def print_tank_for(seconds, frams_per_sec):
    # Print tank for x seconds at y frams per sec
    # Generate a random location
    current_location = [random.randint(0, TANK_WIDTH-1), random.randint(0, TANK_HEIGHT-1)]
    # Determine the length of printing
    print_timer = int(time.localtime(time.time()).tm_sec) + seconds
    print_time_temp = int(time.localtime(time.time()).tm_sec)
    print_time = int(time.localtime(time.time()).tm_sec)
    # Printing
    while print_time != print_timer:
        present_location = [int(current_location[0]), int(current_location[1])]
        next_location = fish_movement(current_location)
        fish_direction = fish_face(next_location, present_location)
        current_location = next_location
        print_tank(current_location, fish_direction, 1/frams_per_sec)
        # Determine if time is up
        if print_time_temp != int(time.localtime(time.time()).tm_sec):
            print_time_temp = int(time.localtime(time.time()).tm_sec)
            print_time = print_time + 1
    # Viloently close window and prevent from printing again until restart
    myPen.bye()
    

##############################################################
#   Main Function
##############################################################
def main_lib():
    print("This is a library function.")


##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main_lib()
