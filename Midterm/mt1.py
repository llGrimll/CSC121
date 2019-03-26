# Print the sum of just the negative numbers and then print the average of
# those numbers

nums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3]
# Your code below:
neg_nums = []
x = 0
for i in range(len(nums)):
    num_value = nums[i]
    if num_value < 0:
        neg_nums.append(num_value)
        x += 1
        # print(neg_nums)

neg_num_total = sum(neg_nums)
neg_num_length = len(neg_nums)
neg_num_average = neg_num_total / neg_num_length

# Your 2 print statements
print(neg_num_total)
print(neg_num_average)
