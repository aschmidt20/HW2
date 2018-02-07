N = int(input())
line = input()
line = line.split(" ")
line_int = []
for entry in line:
    line_int.append(int(entry))
line = line_int
sorted = list(line)
sorted.sort()
if sorted != line:
    i = 0
    mismatches = 0
    mismatch_list = []
    while i < len(line):
        if line[i] != sorted[i]:
            mismatches += 1
            mismatch_list.append(i)
        i += 1

    if(len(mismatch_list) == 2):
        print("SWAP " + str(line[mismatch_list[0]]) + " " + str(line[mismatch_list[1]]))
    elif(len(mismatch_list) >= 3):
        reverse_list = line[(mismatch_list[0]):(mismatch_list[len(mismatch_list)-1]+1)]
        sort_mis = list(reverse_list)
        sort_mis.sort()
        reverse_list.reverse()
        if reverse_list == sort_mis:
            print("REVERSE " + str(line[mismatch_list[0]]) + " " + str(line[mismatch_list[len(mismatch_list)-1]]))
        else:
            print("NOT POSSIBLE")

    else:
        print("NOT POSSIBLE")
else:
    print("SORTED")

