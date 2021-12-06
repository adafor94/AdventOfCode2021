fishes = open("input.in", "r").read().strip().split(',')
fishes = [int(fish) for fish in fishes]
state = [0]*9     #How many fishes in each state

for fish in fishes:
  state[fish] += 1

def calcNextState(state):
  next = [0]*9
  for i in range(9):
    if i == 6:
      next[i] = state[0] + state[7]
    else:
      next[i] = state[(i+1)%9]
  return next

state1 = state
state2 = state

for _ in range(80): #Iterations part 1
  state1 = calcNextState(state1)
for _ in range(256):      #Iterations part 2
  state2 = calcNextState(state2)

print("Part1:", sum(state1))
print("Part2:", sum(state2))
