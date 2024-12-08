def func(nums):
    if not nums:
        return 0
    unique_nums = set(nums)
    longest_length = 0
    for number in unique_nums:
        if number - 1 not in unique_nums:
            current_number = number
            streak_length = 1
            while current_number + 1 in unique_nums:
                current_number += 1
                streak_length += 1

            longest_length = max(longest_length,streak_length)
        return longest_length

print(func([9, 1, 4, 7, 3, 2, 8, 5, 6]))
print(func([100, 4, 200, 1, 3, 2]))
print(func([0,0]))