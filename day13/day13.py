d, folds = open("input.in", "r").read().strip().split('\n\n')
d = d.split('\n')
folds = folds.split('\n')

dots = set()
for dot in d:
  temp = dot.split(',')
  x,y = int(temp[0]), int(temp[1])
  dots.update({(x,y)})

folds = [x.split(' ')[2].split('=') for x in folds]

for f in folds:
  newSetOfDots = set()
  axis, pos = f[0], int(f[1])
  for x,y in dots:
    if axis == 'x' and x > pos:
      newSetOfDots.update({(2*pos-x, y)})
    elif axis == 'y' and y > pos:
      newSetOfDots.update({(x,2*pos-y)})  
    else:
      newSetOfDots.update({(x,y)})  
  dots = newSetOfDots

xMax = max([x for x,y in dots])
yMax = max([y for x,y in dots])

for y in range(yMax+1):
  s = ''
  for x in range(xMax+1):
    if (x,y) in dots:
      s += '#'
    else:
      s += '.'
  print(s)
