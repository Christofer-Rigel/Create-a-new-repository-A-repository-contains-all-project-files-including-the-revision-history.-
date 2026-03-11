def min_flips(arr):
    # Count number of 0s and 1s
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    
    # To make all elements equal, flip the smaller group
    return min(count_0, count_1)

# Example usage:
arr = [1, 0, 1, 1, 0, 0, 1]
print("Minimum flips needed:", min_flips(arr))
