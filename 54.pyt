
x = input("Enter the string: ")

def find_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# Example usage
input_string = x
all_substrings = find_substrings(input_string)

print("All substrings of the string are:")
for substring in all_substrings:
    print(substring)
