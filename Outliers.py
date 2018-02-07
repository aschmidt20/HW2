# Parse Inputs 
first_line = [int(x) for x in input().split()]
N = first_line[0]
K = first_line[1]

# Sort the available bins 
k_vals = sorted([int(x) for x in input().split(" ")])

# Make a list of the differences between any middle bins
differences = [int((j-i)/2) for i, j in zip(k_vals[:-1], k_vals[1:])]
# Account for any ID being before the first bin 
# Account for any ID being in between any available bins 
# Account for any ID being past the last bin 
differences = [k_vals[0]] + differences + [N - 1 - k_vals[-1]]

# Max of these is the furthest possible distance 
print(max(differences))
