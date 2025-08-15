def is_power_of_two(n):
    if n <= 0:  # Base case: numbers less than or equal to 0 are not powers of 2
        return False
    if n == 1:  # Base case: 2^0 is 1
        return True
    return n % 2 == 0 and is_power_of_two(n // 2)  # Recursively check if n/2 is a power of 2

# Example usage:
num = int(input("Enter a number: "))
if is_power_of_two(num):
    print(f"{num} is a power of 2")
else:
    print(f"{num} is NOT a power of 2")