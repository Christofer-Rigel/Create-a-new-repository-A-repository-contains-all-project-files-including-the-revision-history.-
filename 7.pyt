def myfunction1(n):
    if n <= 0:
        return
    for i in range(0, n + 1):
        print("Codingal")
    myfunction1(n // 2)
    myfunction1(n // 3)

def myfunction2(n):  
    if n <= 1:
        return
    print("Codingal")
    myfunction2(n - 1)

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    
    print("\nRunning myfunction1(n):")
    myfunction1(n)
    
    print("\nRunning myfunction2(n):")
    myfunction2(n)
