def elements(list1, list2):
    return list(set(list1) & set(list2))

print(elements([1, 2, 3], [2, 3, 4]))
print(elements([1, 1, 2], [1, 3]))
print(elements([], [1, 2]))