def revstr(s):
    if len(s) == 1:
        return s[0] 
    firstchar = s[0]
    return revstr(s[1:]) + firstchar

s = input("Enter a string: ")
print(revstr(s))
