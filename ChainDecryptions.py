N = int(input())
decrypt = []
for i in range(N):
    line = input()
    line = line.split(" ")
    decrypt.append(line)
position = 0
while position < len(decrypt):
    megabits = int(decrypt[position][0])
    continue_cracking = True
    iter = position + 1
    while position != iter and continue_cracking:
        if megabits >= int(decrypt[iter][1]):
            continue_cracking = True
            megabits = megabits - int(decrypt[iter][1])
            megabits = megabits + int(decrypt[iter][0])
            iter += 1
            iter = iter % len(decrypt)
        else:
            continue_cracking = False
    if continue_cracking == True:
        print(position)
        break
    position += 1