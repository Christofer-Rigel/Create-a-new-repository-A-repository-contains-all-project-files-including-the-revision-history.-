def loa(arr):
    if len(arr) == 0:
        return 0
    return 1 + loa(arr[1:])
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(loa(arr))