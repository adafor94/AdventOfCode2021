input = open("input.in", "r").read().strip().split('\n')
input = [row.split(' -> ') for row in input]

setOfAllPoints1, setOfAllPoints2, setOfDangerousPoints1, setOfDangerousPoints2 = set(), set(), set(), set()
count1 = count2 = 0

for start, end in input:
  x1, y1 = start.split(',')
  x2, y2 = end.split(',')
  x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
  r = max(abs(x1-x2), abs(y1-y2))                       #range is biggest difference in x and y
  dx = (x2-x1)/abs(x1-x2) if abs(x1-x2) > 0 else 0      #normalized hange in x. if-condition to avoid division by zero
  dy = (y2-y1)/abs(y1-y2) if abs(y1-y2) > 0 else 0      #normalized change in y. if-condition to avoid division by zero

  for i in range(r+1):
    x = x1 + i*dx
    y = y1 + i*dy 
    
    #Part1
    if x1 == x2 or y1 == y2: 
      if (x,y) in setOfAllPoints1:
        if (x,y) not in setOfDangerousPoints1:
          count1 += 1
          setOfDangerousPoints1.add((x,y))
      else: 
        setOfAllPoints1.add((x,y))
    
    #Part2
    if (x,y) in setOfAllPoints2:  
      if (x,y) not in setOfDangerousPoints2:
        count2 += 1
        setOfDangerousPoints2.add((x,y))
    else:
      setOfAllPoints2.add((x,y))

print("Part1:", count1)
print("Part2:", count2)