import functools 
input = open("input.in", "r").read().strip()
hexToBinary = dict({'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', 
                    '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'})

global part1
part1 = 0

def parse(bits):     

  global part1
  v = int(bits[:3], 2)        # get version
  t = int(bits[3:6], 2)       # get type
 
  part1 += v              
  bits = bits[6:]             # update bits

  if t == 4:                    # Literal
    value = ''
    while bits[0] == '1':
      value += bits[1:5]
      bits = bits[5:]
    value += bits[1:5]
    bits = bits[5:]
    return bits, int(value,2)
  else:                         # operator
    values = []
    lt = bits[0]
    if lt == '1':                 #  packets
      l = int(bits[1:12], 2)      # number of packets
      bits = bits[12:]
      for x in range(l):          # parse l number of packets
        (bits, value) = parse(bits)
        values.append(value)      # save all subpackets return values
    else:                         #  bits
      l = int(bits[1:16], 2)      # number of bits
      bits = bits[16:]
      subpackets = bits[:l]
      while subpackets:           # parse l number of bits
        (subpackets, value) = parse(subpackets)    
        values.append(value)      #save subpackets return value
      bits = bits[l:]
    if t == 0:                    # calculate value depending on t
      return bits, sum(values)
    elif t == 1:
      return bits, functools.reduce(lambda x, y: x * y, values, 1)
    elif t == 2:
      return bits, min(values)
    elif t == 3:
      return bits, max(values)
    elif t == 5:
      return bits, values[0] > values[1]
    elif t == 6:
      return bits, values[0] < values[1]
    elif t == 7:
      return bits, values[0] == values[1]

bits = ''
for c in input:
  bits += hexToBinary[c]

_, value = parse(bits)
print("Part1:", part1)
print("Part2:", value)
