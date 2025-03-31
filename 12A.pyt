choice  = input("Enter either HCF stands as 1 or LCM stands as 2: ")
if choice == "1" or choice == "HCF" :
    numberlargest = int(input("Enter the largest number: "))
    numberSmallest = int(input("Enter the smallest number: "))
    while(numberSmallest) :
        numberStore = numberSmallest
        numberSmallest = numberlargest % numberSmallest
        numberLargest = numberStore
    print(f"The HCF is {numberStore}")
elif choice == "2" or choice == "LCM" :  
    numberlargest = int(input("Enter the largest number: "))
    numberSmallest = int(input("Enter the smallest number: "))
    hcf = numberlargest % numberSmallest
    lcm = (numberlargest * numberSmallest) / hcf
    print(f"The LCM is {lcm}")
else :
    print("Invalid choice, please select either HCF or LCM")
