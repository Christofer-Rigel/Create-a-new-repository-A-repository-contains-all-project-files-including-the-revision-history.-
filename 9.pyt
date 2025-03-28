def print_factors(numbers):
    print("the factors of", numbers, "are:")
    for i in range(1, numbers + 1):
        if numbers % i == 0:
            print(i)

number = int(input("Enter your number to find its fractions please note that it might go wrong :                    "))
print_factors(number)