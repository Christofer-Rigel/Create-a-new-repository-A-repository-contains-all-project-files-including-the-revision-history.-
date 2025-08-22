
x = int(input("Enter the number to govern the limit: "))

def print1to10(n):
    if (n>x):
        return
    print(n)
    print1to10(n+1)
print1to10(1)