

##############################################################
#   Libraries
##############################################################
import random
import time
import os
import sys


##############################################################
#   Variable Definition
##############################################################
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

    if foodr > FOOD_MAX:
        foodr = FOOD_MAX

    info[6] = foodr


def consumed(hour, info):
    # Consumption per hour
    for x in range (1, hour):
        info[5] = info[5] * (0.9995 - abs(info[6]-100)/100 * 0.0001)
        info[6] = info[6] * 0.992


def check_save_file():
    # Check for save file and load info
    exists = os.path.isfile('data')
    not_empty = os.stat('data').st_size
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


##############################################################
#   Main Function
##############################################################
def main():
    # Check for previous save file and load
    info = check_save_file()
    # Start of Program
    while 1:
        # Print Menu and Request Input
        print_menu()
        time.sleep(1)
        selection = int(input("Select -> "))
        print(selection)
        time.sleep(1)
        os.system('clear')
        # Switch Select Input
        if selection == 1:
            print_status(info)
        elif selection == 2:
            info[5] = 120
            info[4] = info[4] * 0.995 * 0.995
            print("Water Changed")
        elif selection == 3:
            feed(info[6], info[5], info)
        elif selection == 4:
            save_file(info)
            print("Progress Saved and Exit")
            sys.exit(4)
        elif selection == 5:
            print("Exiting without Saving...")
            sys.exit(5)
        elif selection == 6:
            delete_save()
            sys.exit(6)
        else:
            print("Invalid Input")
            time.sleep(1)
        # System Time Out for 1 Second
        time.sleep(1)


##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()