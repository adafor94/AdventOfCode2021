import fileinput

input = open("input.in", "r").read().strip().split('\n')
occurences = [0] * len(input[0])

for num in input:       #Simply counts the occuranses of 1 and 0. occurances[i] > 0 means more 1s than 0s. 
  for i in range(len(num)):
    occurences[i] += 1 if num[i] == '1' else -1 

def part2filter(numbers, m):      #Filters according to instructions. m is used for filtering on most common/least common 
  for i in range(len(numbers[0])):
    if len(numbers) <= 1:
      return numbers
    ones = []
    zeros = []
    for num in numbers:
      if num[i] == '1':
        ones.append(num)
      else:
        zeros.append(num)

    if m:
      numbers = ones if len(ones) >= len(zeros) else zeros
    else:
      numbers = ones if (len(ones) < len(zeros)) and len(ones) != 0 else zeros
  return numbers

o = part2filter(input, 1)[0]    #Contains the one element left
c = part2filter(input, 0)[0]     #Containts the one element left

g = e = 0
for i in range(1, len(occurences)+1):
  g += (occurences[-i] > 0) * 2**(i-1)
  e += (not occurences[-i] > 0) * 2**(i-1)

print("Part1:", g*e)
print("Part2:", int(o,2) * int(c,2))