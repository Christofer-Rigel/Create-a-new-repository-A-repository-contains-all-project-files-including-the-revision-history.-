def Binarytodecimal(Binaryinput):
    # Convert binary string to a decimal number
    resultInteger = 0
    # Iterate over the binary digits
    for i in range(len(Binaryinput)):
        # Calculate the position value in decimal
        resultInteger = resultInteger * 2 + int(Binaryinput[i])
    return resultInteger

# Get binary input from the user
Binary = input("Enter your binary number: ")
print("Integer equivalent:", Binarytodecimal(Binary))