def noofbits(n):
    # Count the number of bits in a number
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count
number = int(input("Enter a number no decimal on the sides please: "))
print("The number of bits in", number, "is", noofbits(number))