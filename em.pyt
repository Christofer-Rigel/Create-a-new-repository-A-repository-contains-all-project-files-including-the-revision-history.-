import random as r 
while True:
    x = r.randint(1, 100)
    print(x)
    print("Isnt correct again")
    if x == 99:
        print("Correct")