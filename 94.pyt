def equilbreumPoint(arr):
    leftSidesum = 0
    rightidesum = 0
    n = len(arr)

    for i in range(n):
        leftSidesum = 0
        rightidesum = 0
        for j in range(i):
            leftSidesum +=1

        for j in range(i + 1, n):
            rightidesum +=arr[j]

        if leftSidesum == rightidesum :
            return i
        
    return -1

arr = [-4,6,2,0,0,1,1,]
print("element                                                                                                                                          :",arr[equilbreumPoint(arr)])