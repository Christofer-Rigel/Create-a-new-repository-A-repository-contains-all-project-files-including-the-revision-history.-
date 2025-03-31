number = int(input("Enter a number: "))
oringinal_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if oringinal_number == reversed_number:
    print(f"{oringinal_number} is a palindrome number")
else:
    print(f"{oringinal_number} is not a palindrome number")