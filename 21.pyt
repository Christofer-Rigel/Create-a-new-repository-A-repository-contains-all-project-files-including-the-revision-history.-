def isEvenOdd( n):
    # XQR with 1 equals n+1
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
number = int(input("Enter a number no decimal on the sides please: "))
if (isEvenOdd(number)):
    print(number,"Is even")
else:
    print(number,"Is odd")