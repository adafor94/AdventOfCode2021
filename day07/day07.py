import math 

crabs = [int(crab) for crab in open("input.in", "r").read().strip().split(',')]
crabs.sort()

def cost1(crabs, x):
  cost = 0
  for crab in crabs:
    cost += abs(crab-x)
  return cost

def cost2(crabs, x):
  cost = 0
  for crab in crabs:
    n = abs(crab-x)         #Steps
    cost += n*(n+1)/2       # Sum of all natural numbers 0 to n
  return cost

x = crabs[int((len(crabs)/2)-1)]  # Middle value of sorted list
print("Part1:", cost1(crabs, x))

x1 = math.floor(sum(crabs)/len(crabs)) # Average rounded down
x2 = math.ceil(sum(crabs)/len(crabs))   # Average rounded up
print("Part2:", int(min(cost2(crabs,x1), cost2(crabs,x2))))
