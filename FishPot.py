
##############################################################
#   Libraries
##############################################################
from H2O import *

##############################################################
#   Variable Definition
##############################################################



##############################################################
#   Function Prototype
##############################################################


##############################################################
#   Main Function
##############################################################
def main():
    # Check for previous save file and load
    info = check_save_file()
    start_hour = time.localtime(time.time()).tm_hour
    looped = False
    # Start of Program
    while 1:
        # Print Menu and Request Input
        print_menu()
        selection = int(input("Select -> "))
        print(selection)
        os.system('cls')
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
        elif selection == 7:
            start_hour = forward(start_hour)
            print("Time has been forwarded")
        elif selection == 8:
            if looped == True:
                print("This option is unavaliable")
                #os.execl(sys.executable, os.path.abspath(__file__))
            else:
                print("Showing the water tank for 10 seconds")
                print_tank_for(10, 60)
                looped = True
        else:
            print("Invalid Input")
            time.sleep(0.5)
        # Check Time Pass
        now_time = time.localtime(time.time())
        if start_hour != time.localtime(time.time()).tm_hour:
            info = consumed(1, info)
            # Update Information
            info[0] = int(now_time.tm_year)
            info[1] = int(now_time.tm_mon)
            info[2] = int(now_time.tm_mday)
            info[3] = int(now_time.tm_hour)
            start_hour = int(now_time.tm_hour)


##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    main()
