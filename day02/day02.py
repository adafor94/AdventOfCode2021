import fileinput

directions = [line.split(' ') for line in open("input.in", "r").read().strip().split('\n')]
horizontal = depth1 = depth2 = 0

for dir in directions:
  value = int(dir[1])
  if dir[0] == 'down':
    depth1 += value
  elif dir[0] == 'up':
    depth1 -= value
  elif dir[0] == 'forward':
    horizontal += value
    depth2 += depth1*value

print("Part1:", depth1*horizontal)
print("Part2:", depth2*horizontal)