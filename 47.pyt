for i in range(-1000,100000000):
    a = i
    b = i / 2
    guess = int(input(f"Enter whats {a} * {b}? :  "))
    if guess == a * b:
        print("Correct!")
    else:
        print("Incorrect!")
    print("The answer is ", a * b)