with open('input', 'r') as f:
    data = f.read().splitlines()



actual_number = ''
numbers = []
flag = False
for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y].isnumeric():
            actual_number += data[x][y]
            for i,j in [(0, 1), (1,1), (-1, -1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1)]:
                try:
                    if not data[x+i][y+j] == '.' and not data[x+i][y+j].isnumeric():
                        #print(data[x+i][y+j])
                        flag = True
                except:
                    pass

            if y == len(data[0])-1:
                print('tu som')
                if flag:
                    #print(actual_number)
                    numbers.append(int(actual_number))
                    flag = False
                actual_number = ''

                
        else:
            if flag:
                #print(actual_number)
                numbers.append(int(actual_number))
                flag = False
            actual_number = ''
        
        

print(sorted(numbers))
print(sum(numbers))
print(len(numbers))