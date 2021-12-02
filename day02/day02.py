import fileinput

directions = [line.split(' ') for line in open("input.in", "r").read().strip().split('\n')]
horizontal = depth1 = depth2 = 0

for dir, value in directions:
  if dir == 'down':
    depth1 += int(value)
  elif dir == 'up':
    depth1 -= int(value)
  elif dir == 'forward':
    horizontal += int(value)
    depth2 += depth1*int(value)

print("Part1:", depth1*horizontal)
print("Part2:", depth2*horizontal)