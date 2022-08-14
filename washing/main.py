from wash_hands import hand_wash, bcolors
import urllib
from stats import look_up

print("Choose an Option")
print("----------")

while True:
  try:
    option = int(input("1 - View stats on coronavirus for a country\n2 - Set a handwash reminder and timer\n0 - to exit\n"))
  except:
    print("Invalid value")

  try:
    if option == 1:
      look_up()
  
    elif option == 2:
      hand_wash()
    elif option == 0:
      break
  except:
    print("Sorry Error occured")



