input = open("input.in", "r").read().strip().split('\n')
ROWS = len(input)
COLS = len(input[0])

#Part1
part1 = 0
lowpoints = []
for i in range(ROWS):
  for j in range(COLS):
    h = input[i][j]
    if (i-1 < 0 or input[i-1][j] > h) and (i+1 > ROWS-1 or input[i+1][j] > h) and (j-1 < 0 or input[i][j-1] > h) and (j+1 > COLS-1 or input[i][j+1] > h): #index inside matrix and values > h
      part1 += int(input[i][j])+1
      lowpoints.append((i,j))   #Save point for part2
print("Part1:", part1)

#Part 2
q = set()           # queue of points
basinSizes = []       # List of all basin sizes
for p in lowpoints:
  visited = set()     # Set of visited points to avoid calculating the same point multiple times
  q.add(p)            # add start point
  while q:
    c = q.pop()
    visited.add(c)
    i, j = c[0], c[1] 

    for k,l in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:         # All neighbours
      if (-1 < k and k < ROWS) and (-1 < l and l < COLS): #If inside matrix
        if (k,l) not in visited and input[k][l] != '9':   #Not already visited and not 9. 
          q.add((k,l))                                    # Add to q
  basinSizes.append(len(visited))                         # Add length

basinSizes.sort(reverse=1)
print("Part2:", basinSizes[0]*basinSizes[1]*basinSizes[2])  