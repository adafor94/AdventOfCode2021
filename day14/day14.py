input = open("input.in", "r").read().strip().split('\n')
template, pairs = input[0], input[2:]

chunks = dict()         # Dict of chunks on form AB -> occurances
count = dict()          # Dict of letter on form A -> occurances
pairs = dict(map(lambda x: x.split(' -> '), pairs)) # Dict of mappings on form AB -> C

# Build chunks and count with start values
for i in range(1, len(template)):
  c = template[i]
  count[template[i]] = count.get(template[i], 0) + 1 

  chunk = template[i-1:i+1]
  chunks[chunk] = chunks.get(chunk, 0) + 1

# Add very first element
count[template[0]] = count.get(template[0], 0) + 1

changes = dict() # Dict of changes this iteration, on form AB -> change

for steps in range(40):
  for k, v in pairs.items():      # For every possible pair
    if k not in chunks.keys():    # If no occurances -> do nothing
      continue
    
    n = chunks[k]                 # else save number of occurances
    chunks[k] = 0                 # And set to zero since all of these are split

    count[v] = count.get(v, 0) + n                      #The count of V is increased by the number of chunks, since one V is inserted for each. 
    changes[k[0]+v] = changes.get(k[0]+v, 0) + n        # Update chunks. Now we got n new k[0]+v and n new v+k[1] since v is inserted in the middle.
    changes[v+k[1]] = changes.get(v+k[1], 0) + n
  
  #Update number of chunks of each type
  for k,v in changes.items():
    chunks[k] = chunks.get(k, 0) + v

  changes = dict()
  if steps == 9:          #Part 1
    print("Part1:", max(list(count.values())) - min(list(count.values())))

print("Part2:", max(list(count.values())) - min(list(count.values())))
