line = input()
line = line.split(" ")
K = int(line[0])
N = int(line[1])
final_used = K-N
cores = K
total_cores = K
while total_cores < N:
    old_total = total_cores
    cores *= 2
    total_cores += cores
    final_used = N - old_total
print(final_used)