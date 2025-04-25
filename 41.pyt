def divide(ourDividend, ourDivisor):

    sign = (-1 if ((ourDividend < 0) ^ (ourDivisor < 0)) else 1)
    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)
    quotientNUmber = 0
    tempNumber = 0
    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += (ourDivisor << i)
            quotientNUmber |= (1 << i)
    if sign == -1:
        quotientNUmber=-quotientNUmber
    return quotientNUmber
a = int(input("enter a for a/b:  "))
b = int(input("enter b for a/b:  "))
print("The result of a/b is: ", divide(a, b))
