import array as a


def minElement(a, size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp, a[i])
    return temp
def maxElement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp, a[i])
    return temp


a = [1,12,123,1234,12345,123456,1234567,12345678,123456789,12345678910]
size =  len(a)
print("Minimum element of array:", minElement(a, size))
print("Maximum element of array:", maxElement(a, size))