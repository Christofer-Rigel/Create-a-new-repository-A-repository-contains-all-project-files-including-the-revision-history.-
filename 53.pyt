def fac(n):
    if(n==1 or n==0):
        return 1
    return n*fac(n-1)
n = int(input("Enter the number: "))
print("Factorial of", n, "is", fac(n))
