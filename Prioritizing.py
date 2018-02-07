# Define variable and construct array 
total_cases, priorities = [int(x) for x in input().split()]

# Construct our array 
cases = []
for i in range(total_cases):
    cases.append(int(input()))
    
cases.sort()

for i in range(priorities):
    print(cases.pop())
