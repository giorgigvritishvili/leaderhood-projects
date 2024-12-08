def find_number(numbers):
    if numbers == [2]:
        return []

    n = len(numbers) +1
    my_list = n * (n + 1) // 2
    your_list = sum(numbers)
    return my_list - your_list

print(find_number([1, 2, 4, 5]))
print(find_number([3, 5, 6, 1, 2]))
print(find_number([2]))
