pairs = open("input.in", "r").read().strip().split('\n')
connections = dict()
paths = []

for pair in pairs:            #Build a dict of all connections
  a,b = pair.split('-')
  connections[a].append(b) if a in connections else connections.update({a: [b]})
  connections[b].append(a) if b in connections else connections.update({b: [a]})

def calcPath(node, path, revisitAllowed, part2):
  path.append(node)
  if node == 'end':             #If end is found. Add to paths and return
    paths.append(path)
    return

  unvisited = connections[node]     #Caves we can go to from here
  for n in unvisited:             
    if n.isupper() or n not in path:      #Check if its allowed
      calcPath(n, path.copy(), revisitAllowed, part2)   #If so, calculate path from here
    elif part2 and revisitAllowed and n != 'start':         # IFor part2
      calcPath(n, path.copy(), False, part2)

calcPath('start', [], revisitAllowed=False, Part2=False)
print("Part1:", len(paths))
paths = []        # Reset 
calcPath('start', [], revisitdAllowed=True, Part2=True)
print("Part2", len(paths))