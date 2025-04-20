# Very simple calculator
x = input("Enter the opeerator: +,-,/,*,%,//,**: ")
y = int(input("Enter the first number: "))
z = int(input("Enter the second number: "))
if x == "+":
    print("The sum of two numbers is: ", y + z)
elif x == "-":
    print("The difference of two numbers is: ", y - z)
elif x == "*":
    print("The product of two numbers is: ", y * z)
elif x == "/":
    print("The division of two numbers is: ", y / z)
elif x == "%":
    print("The modulus of two numbers is: ", y % z)
elif x == "//":
    print("The floor division of two numbers is: ", y // z)
elif x == "**":
    print("The exponent of two numbers is: ", y ** z)
else:
    print("Invalid operator")