def sum_floored(numbers):
    return sum(int(num) for num in numbers if num > 0)

print(sum_floored([1, -4, 7, 12]))
print(sum_floored([-1.5, 2.7, -3.3, 4.8]))
print(sum_floored([]))
print(sum_floored([-1, -2, -3]))