import fileinput

numbers = [int(x) for x in open("input.in", "r").read().strip().split('\n')]
part1 = part2 = 0

for i in range(1, len(numbers)):
  part1 += numbers[i] > numbers[i-1]
  part2 += i > 2 and numbers[i] > numbers[i-3]

print("Part1:", part1)
print("Part2:", part2)