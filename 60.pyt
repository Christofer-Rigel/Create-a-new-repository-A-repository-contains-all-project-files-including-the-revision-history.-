def recursive_input():
    num = int(input("Enter your number : "))
    if num < 0:
        print("Number -ve")
    else:
        print("Number +ve")
        recursive_input()

recursive_input()