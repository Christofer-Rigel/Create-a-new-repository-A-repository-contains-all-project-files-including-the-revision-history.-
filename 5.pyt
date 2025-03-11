def multiply_once(a, b):
    return a * b

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiply_once(num1, num2)
print(f"The result of multiplying {num1} and {num2} is: {result}")

def multiply_n_times(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiply_n_times(num1, num2)
print(f"The result of multiplying {num1} and {num2} using N iterations is: {result}")
