import math 

crabs = [int(crab) for crab in open("input.in", "r").read().strip().split(',')]
crabs.sort()   
#Part 1
x = crabs[int((len(crabs)/2)-1)]  # Median value
print("Part1:", sum(abs(crab-x) for crab in crabs)) #Sum of distance to median value

#Part2. Answer is the average rounded up or down
x1, x2 = math.floor(sum(crabs)/len(crabs)), math.ceil(sum(crabs)/len(crabs)) 

cost = lambda crabs, x: sum(abs(crab-x)*(abs(crab-x)+1)/2 for crab in crabs) #sum of the costs. Using 1+2+3+..+n = n*(n+1)/2
print("Part2:", int(min(cost(crabs,x1), cost(crabs,x2))))