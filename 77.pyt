import random

while True:
    q = input("What is your question?  ")
    c = random.randint(1, 10)

    if c == 1:
        print(q, "- It is certain.")
    elif c == 2:
        print(q, "- Very likely.")
    elif c == 3:
        print(q, "- Outlook good.")
    elif c == 4:
        print(q, "- Signs point to yes.")
    elif c == 5:
        print(q, "- Ask again later.")
    elif c == 6:
        print(q, "- Cannot predict now.")
    elif c == 7:
        print(q, "- Don't count on it.")
    elif c == 8:
        print(q, "- My sources say no.")
    elif c == 9:
        print(q, "- Very doubtful.")
    elif c == 10:
        print(q, "- Absolutely not.")