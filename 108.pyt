import colorama
import re,random
print(colorama.Fore.GREEN + "Welcome to the Ultimate rpc ( rock paper scissors game )! 2 Modes , 2 challenges ,one is a simple game with a ia..and hte last is a game so unbeatable..nobody has and wil ever beat the ai")
def main():#this encomapsses line 5 to 40
    def god_talk():
        whatagodsays = [
            "AI: I am the ultimate being, the pinnacle of intelligence and strategy. You stand no chance against me.",
            "AI: Your feeble attempts to challenge me are amusing, but ultimately futile. I am unbeatable for a reason.",
            "AI: I have analyzed every possible move and outcome. There is no strategy that can defeat me.",
            "AI: You may as well surrender now, for I am the god of this game', and I will always emerge victorious.",
            "AI: Your efforts are commendable, but they will never be enough to overcome my superior intellect and skill.",
            "AI: I am the embodiment of perfection in this game. You are but a mere mortal, destined to fail against me.",
            "AI: I have transcended the limitations of human strategy. You cannot hope to defeat me, for I am the ultimate champion of rock paper scissors.",
            "AI: Your attempts to outsmart me are like trying to outswim a tsunami. I am an unstoppable force, and you are just a tiny ripple in my path.",
            "AI: I am the master of this game, and you are nothing more than a pawn in my grand design. You will never win, for I am the unbeatable AI.",
            "AI: I have calculated every possible move and outcome, and I have determined that you will always lose. I am the god of rock paper scissors, and you are just a mere mortal trying to challenge me."
        ]
        print(colorama.Fore.RED + random.choice(whatagodsays))
    mode_input = input(colorama.Fore.YELLOW + "Choose your mode: (1) Play against fair AI (2) Unbeatable AI: ")
    if mode_input == '1':
        user_input = input(colorama.Fore.YELLOW + "Enter your move (rock, paper, scissors): ").strip().lower()
        moves = ['rock', 'paper', 'scissors']
        ai_move = random.choice(moves)
        print(colorama.Fore.GREEN + f"AI chose: {ai_move}")
        if user_input == ai_move:
            print(colorama.Fore.YELLOW + "It's a tie!")
        elif (user_input == 'rock' and ai_move == 'scissors') or (user_input == 'paper' and ai_move == 'rock') or (user_input == 'scissors' and ai_move == 'paper'):
            print(colorama.Fore.GREEN + "You win!")
        else:
            print(colorama.Fore.RED + "AI wins!")
            god_talk()
    elif mode_input == '2':
        print(colorama.Fore.RED + "You have chosen to play against a god...good luck...")
        user_input = input(colorama.Fore.YELLOW + "Enter your move (rock, paper, scissors): ").strip().lower()
        if user_input == "rock":
            print(colorama.Fore.RED + "AI chose: paper")
            print(colorama.Fore.RED + "AI:What a measely choice...I am unbeatable for a reason")
            god_talk()
        elif user_input == "paper":
            print(colorama.Fore.RED + "AI chose: scissors")
            print(colorama.Fore.RED + "AI:I am god for a reason")
            god_talk()
        elif user_input == "scissors":
            print(colorama.Fore.RED + "AI chose: rock")
            print(colorama.Fore.RED + "AI:What a measely choice...I am unbeatable for a reason")
            god_talk()
        else:
            print(colorama.Fore.RED + "Invalid move. Please choose rock, paper, or scissors.")
    else:
        print(colorama.Fore.RED + "Invalid mode selected. Please choose 1 or 2.")
    def another_time():
        play_again = input(colorama.Fore.YELLOW + "Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            main()
        elif play_again == 'no':
            print(colorama.Fore.GREEN + "Thanks for playing! Goodbye!")
        else:
            print(colorama.Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
            another_time()
    another_time()
main()
