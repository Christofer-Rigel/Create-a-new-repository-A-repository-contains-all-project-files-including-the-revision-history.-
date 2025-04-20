def power_of_8(number):
    # Check if the number is positive
    if number <= 0:
        return False

    # Keep dividing the number by 8 while it's divisible by 8
    while number % 8 == 0:
        number //= 8

    # If the final result is 1, the number is a power of 8
    return number == 1

# Input from the user
number = int(input("Enter a number: "))
if power_of_8(number):
    print("\nThe number is a power of 8")
else:
    print("\nThe number is not a power of 8")