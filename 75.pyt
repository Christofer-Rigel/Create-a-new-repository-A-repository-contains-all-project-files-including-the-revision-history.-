import random as r
# names of verable cant contain spaces
def tryagianorfail():

    game_number = r.randint(1,1000)
    cd = r.randint(1,10)
    clue = game_number / cd
    print("If my number is / by ", cd , "then it equals", clue)
    guess  = int(input("enter what you think is the number here :  "))
    if (guess == game_number) :     
        print("correct its",game_number)


ask = input("do you wanna try again yes or no ?  ")
if (ask == "yes") : 
    tryagianorfail()
elif (ask == "no") :
    print("better luck next time")
else :
    print("invalid character")