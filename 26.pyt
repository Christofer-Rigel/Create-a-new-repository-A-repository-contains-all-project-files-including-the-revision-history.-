def find_rightmost_set_bit(num):
    if num == 0:
        return "No set bit found (number is 0)."
    
    # Find the position of the rightmost set bit
    position = (num & -num).bit_length()
    
    # Return the position
    return position

# Example Usage
number = int(input("Enter a number: "))
result = find_rightmost_set_bit(number)
print(f"The rightmost set bit is at position: {result}")