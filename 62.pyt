def arrayTotalSum(a):
    lenght = len(a)
    if lenght == 1:
        return a[0]
    
    return a[0] + arrayTotalSum(a[1:])
a = [1,2,3,4,5,6]
print("array total sum : ", arrayTotalSum(a))