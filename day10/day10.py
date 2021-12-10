lines = open("input.in", "r").read().strip().split('\n')
part1 = 0
part2 = []

penalty = lambda x: (x == ')') * 3 + (x == ']') * 57 + (x == '}') * 1197 + (x == '>') * 25137         #Simply checks the character and returns penalty score

#Part1
for line in lines:          #Put opening character on stack, match closing characters with top of stack. If its wrong, add penalty score
  stack = []
  prev = part1
  for c in line:
    if c == ')':
      if stack.pop() != '(':
        part1 += penalty(c)
        break
    elif c == ']':
     if stack.pop() != '[':
        part1 += penalty(c)
        break
    elif c == '}':
     if stack.pop() != '{':
        part1 += penalty(c)
        break
    elif c == '>':
     if stack.pop() != '<':
        part1 += penalty(c)
        break
    else:
      stack.append(c)

  #Part 2
  score = 0
  if part1 == prev:          # Line not corrupt
    while(stack):                     #Symbols on stack == line incomplete
      c = stack.pop()
      if c == '(':
        score = score * 5 + 1
      elif c == '[':
        score = score * 5 + 2
      elif c == '{':
        score = score * 5 + 3
      elif c == '<':
        score = score * 5 + 4
    part2.append(score)         #append line score to list of scores

part2.sort()

print("Part1", part1)
print("Part2:", part2[int(len(part2)/2)])           #Take the middle score
      
