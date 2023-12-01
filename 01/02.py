with open('input', 'r') as f:
    data = f.read().splitlines()


numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

sum = 0

for line in data:
    digits = []
    for index,sign in enumerate(line):
        if sign.isnumeric():
            digits.append(int(sign))
        else:
            for num in numbers:
                length = len(num)
                if num.startswith(sign) and (line[index:index+length] == num):
                    digits.append(numbers[num])
    sum += int(f'{digits[0]}{digits[-1]}')

print(sum)
