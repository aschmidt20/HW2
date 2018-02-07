#NOT FINISHED
#TIMES OUT ON 2 CASES


first_line = input()
first_line = first_line.split(" ")
N = int(first_line[0])
K = int(first_line[1])
line = input()
line = line.split(" ")
max_shift = 0
i = 0
while i <= int(N-1):
    if i not in line:
        min_dist = 1000000000000
        for value in line:
            dist = abs(int(value) - i)
            if dist < min_dist:
                min_dist = dist
        if min_dist > max_shift:
            max_shift = min_dist
        i += 1
print(max_shift)