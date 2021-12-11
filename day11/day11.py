rows = open("input.in", "r").read().strip().split('\n')
ROWS = len(rows)
COLS = len(rows[0])
energyLevels = [int(n) for row in rows for n in row]

def getAdj(i):
  if i%COLS == 0:       # If first in row
    adj = [i-COLS, i-COLS+1, i+1, i+COLS, i+COLS+1]
  elif (i+1)%COLS == 0: # If last in row
    adj = [i-COLS-1, i-COLS, i-1, i+COLS-1, i+COLS]
  else:  
    adj = [i-COLS-1, i-COLS, i-COLS+1, i-1, i+1, i+COLS-1, i+COLS, i+COLS+1]
  adj = list(filter(lambda x: x >= 0 and x < ROWS*COLS, adj))   #Filter index out of bound
  return adj

simulFlash = False
step = flashes = 0

while not simulFlash or step < 101:     # Just in case simulflash happens before 100 steps
  if step == 100:       #After 100 steps, print part1 answer
    print("Part1:", flashes)
  step += 1

  prevFlashes = flashes                       # Keep track of number of flashes each step to solve part 2
  cont = True                                 # To indicate new flashes
  for i in range(len(energyLevels)):          # Increase each by 1
    energyLevels[i] = energyLevels[i]+1

  while cont:
    cont = False                              # Reset
    for i in range(len(energyLevels)):        #Check every octopuses light level
      if energyLevels[i] > 9:
        flashes += 1
        cont = True
        energyLevels[i] = 0
        adj = getAdj(i)                       #Calc adjacent indexes
        for a in adj:
          if energyLevels[a] != 0:            # level == 0 means this octopus already flashes during this step -> Dont increase
            energyLevels[a] = energyLevels[a] + 1

  if prevFlashes + ROWS*COLS == flashes:      # If all ocotpuses flashed print answer part2 and quit
    print("Part2:", step)
    simulFlash = True