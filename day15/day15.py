from queue import PriorityQueue
import sys

input = open("input.in", "r").read().strip().split('\n')
ROWS = len(input)
COLS = len(input[0])
moves = [(1,0),(0,-1), (-1,0), (0,1)]
numbers = [] 

for line in input:
  numbers.append([int(num) for num in line])

def run(numbers, times):
  q = PriorityQueue()
  q.put((0,0,0))
  distances = dict()
  distances[(0,0)] = 0

  while not q.empty():
    (dist, x, y) = q.get()

    for (dx,dy) in moves:
      x1 = x+dx
      y1 = y+dy
      if x1 < 0 or x1 >= ROWS*times or y1 < 0 or y1 > COLS*times:         # Index out of bounds
        continue  

      val = numbers[x1%ROWS][y1%COLS] + x1 // ROWS + y1 // COLS       # Calc value
      while val > 9:
        val -= 9

      if dist + val < distances.get((x1,y1), sys.maxsize):            
          distances[(x1,y1)] = dist + val
          q.put((dist + val, x1, y1))

  return distances[(len(numbers)*times-1, len(numbers[0])*times-1)]

print("Part1:", run(numbers,1))
print("Part2:", run(numbers,5))