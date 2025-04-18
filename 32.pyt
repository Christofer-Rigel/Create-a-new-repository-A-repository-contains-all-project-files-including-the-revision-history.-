def powerOf4(number):

    count = 0
    if(number & (~(number & (number - 1)))):
        return 0
    while (number > 1):
        number >> 1
        count += 1

    if (count % 2 == 0):
        return True
    else:
        return False
number = int(input("Enter a number: "))
if (powerOf4(number)):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")
