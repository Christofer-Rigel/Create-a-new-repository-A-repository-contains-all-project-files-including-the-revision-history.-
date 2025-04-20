# very simple trafic light simulator
import random
while True:
    c = random.choice(["Red", "Green", "Yellow"])
    if c == "Red":
       print("Stop 🔴 ")
    elif c == "Green":
       print("Go 🟢")
    elif c == "Yellow": 
       print("Wait 🟡")
    else:
       print("Invalid color")
    ask = input("Do you want to continue? (y/n): ")
    if ask.lower() != 'y':
        break