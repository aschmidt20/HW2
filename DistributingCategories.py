num_values = int(input())
dict = {}
max_val = 0
max = 0
for i in range(num_values):
    value = int(input())
    if value in dict:
        dict[value] += 1
    else:
        dict[value] = 1
for index in dict:
    if dict[index] > max_val:
        max = index
        max_val = dict[index]
print(max)