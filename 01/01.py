with open('input', 'r') as f:
    data = f.read().splitlines()

print(data)


sum = 0

for line in data:
    nums = []
    for i in line:
        if i.isnumeric():
            nums.append(i)
    sum += int(f'{nums[0]}{nums[-1]}')

print(sum)
