import array as arr
import math


def arrayMean(arr, arr_size):

    total_sum = 0
    for i in range(0,arr_size):
        total_sum += arr[i]
    return

def arrayMedian(arr,arr_size):
    sorted(arr)

    if arr_size % 2 != 0:
        return float(arr[int(arr_size/2)])
    
    return float((arr[int(arr_size/2)]) + arr[int(arr_size/2)]/2.0)

arr = list(range(1, 251))
arr_size = len(arr)
print("Mean =" , arrayMean(arr, arr_size))
print("Median=" , arrayMedian(arr, arr_size))