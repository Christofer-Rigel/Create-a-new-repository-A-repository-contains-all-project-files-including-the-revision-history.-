import random as r

x = r.randint(1, 64)
def alphannenturimca(x):

    for i in range(x):
        print(chr(64+i), end = " ")
    a = input("Do you want to repeat the process? (yes/no): ")
    if a == "yes":
        alphannenturimca(x)
    elif a == "no":
        print("Goodbye!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
alphannenturimca(x)
x = r.randint(1, 64)
