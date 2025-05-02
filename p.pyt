x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))
z = input("Please enter one of these: '*', '**', '+', '-', '/', '//': ")

if z == '**':
    result = x ** y
elif z == '+':
    result = x + y
elif z == '-':
    result = x - y
elif z == '/':
    result = x / y
elif z == '*':
    result = x * y
elif z == '//':
    result = x // y
else:
    result = "Invalid operator"

print("Result:", result , "This is the result of " , x , y , "These are the numbers and finally the operator" , z)
