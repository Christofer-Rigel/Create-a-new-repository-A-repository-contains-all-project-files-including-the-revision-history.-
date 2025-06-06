def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twosteps = 0
    onesteps = 0

    if (stairs>=2):
        twosteps = ways(stairs-2)
        onesteps = ways(stairs-1)
    return twosteps + onesteps
    
stairs = int(input("Enter number of steps:  "))

print("Number to ways to climb : ", ways(stairs))