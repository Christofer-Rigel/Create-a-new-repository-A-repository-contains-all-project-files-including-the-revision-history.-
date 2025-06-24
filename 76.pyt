import random as r

game_number = r.randint(1,10000)
n = r.randint(1,10)
lives = n
print("lives:",lives)
clue = game_number / n
print("If I am / by",n , "then  equal",clue,"what am I")
guess = int(input("Enter your guess for what the unknown number is :  "))
if (guess == game_number):
    print("correct,सही")
elif (guess != game_number):
    offset = game_number - guess
    print("wrong it was",game_number,"you were",offset,"off")
else:
    print("INVALID INPUT")