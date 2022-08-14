import time
import sys

class bcolors:
    ORANGE = '\033[93m'
    ENDC = '\033[0m'
    BLUE = '\033[94m'

def hand_wash():
  print(bcolors.ORANGE + "Welcome to hand wash reminder" + bcolors.ENDC +" \U0001F9FC")
  print(bcolors.BLUE + "-----------------------------" + bcolors.ENDC)
  name = input("What's your name ? ")
  reminder = input("In the format of hh:mm:ss enter how long to wait before sending out the reminder (or 0 to start immediately): ")
  if reminder == "0":
    pass
  
  else:
    try:
      reminder = reminder.split(":")
      seconds = (int(reminder[0]) * 3600) + (int(reminder[1]) * 60) + int(reminder[2])
    except:
      print("Invalid input")

    s0 = '' if int(reminder[0]) == 1 else 's'
    s1 = '' if int(reminder[1]) == 1 else 's'
    s2 = '' if int(reminder[2]) == 1 else 's'

    print(f"Okay, I will remind you in {reminder[0]} hour{s0}, {reminder[1]} minute{s1} and {reminder[2]} second{s2}")

    time.sleep(seconds)

  print("\U0001F9FC" + "  Hi " + name + ", wash your hands for 20 seconds")
  for i in range(1,21):
    time.sleep(1)
    sys.stdout.write( bcolors.ORANGE + str(i) + " " + bcolors.ENDC)
    sys.stdout.flush()
  print("\n" + "\U0001F64C" + "   finished!")
