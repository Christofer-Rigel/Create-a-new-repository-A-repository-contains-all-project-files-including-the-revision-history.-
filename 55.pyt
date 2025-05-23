def function1(n):
    if n <= 1:
        return n
    return function1(n-1) + function1(n-2)

def function2(n):
    if n <= 1:
        return n
    for i in range(n):
        function2(n-1)

# Estimating Time Complexity:
# function1 follows the Fibonacci pattern -> O(2^n)
# function2 has nested recursion -> O(n!)