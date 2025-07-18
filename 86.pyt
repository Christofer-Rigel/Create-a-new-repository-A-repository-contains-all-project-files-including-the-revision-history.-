def leaders(a, a_size):
    currentmax = a[a_size -1]
    leaders_list = [currentmax]
    for i in range(a_size -2, -1, -1):
        if currentmax < a[i]:
            currentmax = a[i]
            leaders_list.append(currentmax)
    for val in reversed(leaders_list):
        print(val)


a = [16,17,4,3,5,245]
leaders(a, len(a))
