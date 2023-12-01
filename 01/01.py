with open('input', 'r') as f:
    data = f.read().splitlines()


sum_values = 0

for line in data:
    nums = []
    for i in line:
        if i.isnumeric():
            nums.append(i)
    sum_values += int(nums[0] + nums[-1])

print(sum_values)
