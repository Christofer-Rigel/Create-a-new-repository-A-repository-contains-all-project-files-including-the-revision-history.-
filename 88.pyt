def calculateprofitusingpytsincewearetoodumbtodothat(arr, arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]
    return profit 
prices = [64354,536,4,7,5,67,85,785,7,63565,764,8,67,8,5,8,56,7,578,6,9,43,5637,6,57,858,5,7847,85,23456345,76,3,4875673565783648756735657836]
profit = calculateprofitusingpytsincewearetoodumbtodothat(prices, len(prices))
print("Max profit: ", profit)