def romantoInt(romanInput):
    romanNumerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultInteger = 0
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]
roman = input("Enter your roman number : ")
print("Integer equivalent : ",romantoInt(roman))