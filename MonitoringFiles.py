num_values = int(input())
array = []
max_val = 0
for i in range(num_values):
    value = input()
    values = value.split(' ')
    if(values[0] == "1"):
        if int(values[1]) > int(max_val):
            max_val = int(values[1])
        array.append(int(values[1]))
    elif(values[0] == "2"):
        if array[-1] == max_val:
            del array[-1]
            if len(array) > 0:
                max_val = max(array)
            else:
                max_val = 0
        else:
            del array[-1]
    elif(values[0] == "3"):
        print(max_val)
