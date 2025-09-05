def min_flips(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print(f"From {i} to ", end="")
            else:
                print(f"{i - 1}")
    if arr[n - 1] != arr[0]:
        print(n - 1)


# Example usage
arr = [0, 1, 1, 0, 0, 0, 1, 1]
print("Array before flips:", arr)
min_flips(arr)

# To demonstrate conversion, we flip groups to make them all 0s
converted = [0] * len(arr)
print("Array after flips:", converted)
