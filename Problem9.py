num_cases = int(input())

         
cases = []


# Construct a list of potential starting cases and a list of running memory
for i in range(num_cases):
    case = [int(x) for x in input().split()]
    case[1] *= -1
    cases.append(case)
        

for i in range(num_cases):
    running_sum = sum(cases[i])
    if running_sum >= 0:
        j = i + 1
        while j % num_cases != i and running_sum >= 0:
            running_sum += sum(cases[j])
            j = (j + 1) % num_cases
        if running_sum >= 0:
            print(i)
            break
