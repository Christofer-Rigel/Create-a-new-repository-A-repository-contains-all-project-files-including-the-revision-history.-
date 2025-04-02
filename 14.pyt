#find LCM
numberlargest = int(input("Enter the largest number: "))
numbersmallest = int(input("Enter the smallest number: "))
jusfor = (numberlargest % numbersmallest)
lcm = (numberlargest * numbersmallest) / jusfor
print("The LCM of", numberlargest, "and", numbersmallest, "is", lcm)