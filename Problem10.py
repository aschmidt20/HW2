num_cases = int(input())
cases = []
for i in range(num_cases):
    cases.append(tuple(int(i) for i in input().split()))
times = []
cases = sorted(cases, reverse = True)

first = cases.pop()
current_time = sum(first)
times.append(first[1])
num_cases += -1
potentials = []

while num_cases:
    potentials = (tup for tup in cases if current_time >= tup[0])
    
    try:
        todo = min(potentials, key = lambda tup : tup[1])
        cases.remove(todo)
        current_time += todo[1]
    except ValueError:
        todo = cases.pop()
        current_time = sum(todo)
    
    num_cases += -1
    times.append(current_time - todo[0])
    
print(int(sum(times)/len(times)))

