def getinnthemalltosurvive(n,num):
    if (n<1 or n>num):
        return
    print(n)
    getinnthemalltosurvive(n-1,num)
    print(n)
n = int(input("Enter the number: "))
getinnthemalltosurvive(n,n)