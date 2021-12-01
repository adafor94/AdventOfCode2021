import fileinput

numbers = open("input.in", "r").read().strip().split('\n')
numbers = [int(x) for x in numbers]

increases1 = increases2 = 0
last1 = last2 = numbers[0]

for i in range(1, len(numbers)):
  if numbers[i] > last1:
    increases1 += 1
  if i >= 3:
    if numbers[i] > last2:
      increases2 += 1
    last2 = numbers[i-2]
  last1 = numbers[i]

print("Part1:", increases1)
print("Part2:", increases2)