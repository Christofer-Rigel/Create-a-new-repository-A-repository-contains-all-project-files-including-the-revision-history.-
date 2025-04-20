#Very simple dice roller
import random
while True:
   Diceroll = random.randint(1, 6)
   if Diceroll == 1:
       print("⚀")
   elif Diceroll == 2:
       print("⚁")
   elif Diceroll == 3:
        print("⚂")
   elif Diceroll == 4:
        print("⚃")
   elif Diceroll == 5:
         print("⚄")
   elif Diceroll == 6:
         print("⚅")
   else:
         print("Invalid Roll")
   play_again = input("Do you want to roll again? (yes/no): ").lower()
   if play_again.lower() != 'yes':
        break