def totalFlips(num1, num2):
    flips = 0
    while(num1 > 0 or num2 > 0):
        t1 = (num1 & 1)
        t2 = (num2 & 1)
        if t1 != t2:
            flips += 1
        num1 = num1 >> 1
        num2 = num2 >> 1
    return flips
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Total number of flips required to convert", num1, "to", num2, "is", totalFlips(num1, num2))
              