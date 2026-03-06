def longest_alternating_subarray(arr):
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        # Check if current and previous elements are alternating
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1  # Reset length if alternation breaks

    return max_len

# Example usage
a = [6, 4, 9, 4, 7, 2, 3, 4, 2, 52]
print("Length of longest alternating subarray:", longest_alternating_subarray(a))