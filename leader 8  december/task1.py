def positive(numbers):
    return sum(num for num in numbers if num > 0)
print(positive([1, -4, 7, 12]))
print(positive([-1, -2, -3, -4]))
print(positive([]))