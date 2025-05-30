
n = int(input("Enter a number: "))

def chifpoww(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4 == 0):
        return chifpoww(n//4)
    return False
if (chifpoww(n)):
    print("Yes, the number is a power of 4")
else:
    print("No, the number is not a power of 4")