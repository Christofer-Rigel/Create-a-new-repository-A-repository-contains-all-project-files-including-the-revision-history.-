def find_missing_number(arr, n):
    # Calculate expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    # Calculate actual sum of the array
    actual_sum = sum(arr)
    # The missing number is the difference
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5]  # Example array where 3 is missing
n = 5  # Total numbers supposed to be from 1 to 5
missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")