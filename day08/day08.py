patterns = open("input.in", "r").read().strip().split('\n')
part1 = part2 = 0
count = {}
zero = {'a','b','c','e','f','g'}
one = {'c','f'}
two = {'a','c','d','e','g'}
three = {'a','c','d','f','g'}
four = {'b','c','d','f'}
five = {'a','b','d','f','g'}
six = {'a','b','d','e','f','g'}
seven = {'a','c','f'}
eight = {'a','b','c','d','e','f','g'}
nine = {'a','b','c','d','f','g'}
replaceDict = dict()

for pattern in patterns:
  digits, outputs = pattern.split('|')
  digits, outputs = digits.strip().split(' '), outputs.strip().split(' ')
  count = {}
  for i in range(len(digits)):
    for c in digits[i]:
      if c in count:
        count[c] += 1
      else:
        count[c] = 1

  count = list(count.items())
  count.sort(key= lambda x: x[1])         # We now have a list sorted by how many times each character appears
  digits.sort(key= lambda x: len(x))       # The observed observered digits sorted my length

  a = set(digits[1]) ^ set(digits[0])   # We know a is the difference between 1 and 7 (shortest and next shortest)
  b = set(count[1][0])                  # b is the next least frequent
  e = set(count[0][0])                  # e is least frequent
  f = set(count[6][0])                  # f is most frequent
  c = set(digits[0]) ^ f                # c is 1, but not f
  d = set(digits[2]) ^ set(digits[0]) ^ b # d is difference between 4, 1 and b
  g = (set(count[2][0])).union(set(count[3][0])) ^ d  # g is third or forth least frequent, but not d

  replaceDict = {a.pop() : 'a', b.pop() : 'b', c.pop() : 'c', d.pop() : 'd', e.pop() : 'e', f.pop() : 'f', g.pop() : 'g'}
 # print(di['a'], di['b'], di['c'], di['d'], di['e'], di['f'] , di['g'] )

  res = ''

  for v in outputs:
    value = set()
    l = len(v)
    if l == 2 or l == 4 or l == 3 or l == 7:
      part1 += 1
    
    for c in v:           #Add corresponding char to the set
      value.add(replaceDict[c])
 
    if value == zero:
      res += '0'
    elif value == one:
      res += '1'
    elif value == two:
      res += '2' 
    elif value == three:
      res += '3' 
    elif value == four:
      res += '4' 
    elif value == five:
      res += '5'
    elif value == six:
      res += '6'
    elif value == seven:
      res += '7'
    elif value == eight:
      res += '8'
    elif value == nine:
      res += '9'

  part2 += int(res)

print("Part1:", part1)
print("Part2:", part2)