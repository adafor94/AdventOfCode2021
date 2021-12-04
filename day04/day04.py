import copy

input = open("input.in", "r").read().strip().split('\n\n')
numbers = input[0].split(',')
boards =  [board.split('\n') for board in input[1:]]

for i in range(len(boards)):
  boards[i] = [row.strip().replace('  ',' ').split(' ') for row in boards[i]]

def checkNum(board, num):     
  for i in range(5):
    for j in range(5):
      if board[i][j] == num:    #Check every element
        board[i][j] = '-1'      # change to -1 to mark number
        return all([elem == '-1' for elem in board[i]]) or all(row[j] == '-1' for row in board)    #Check if row or col is bingo
  return False

def bingo(boards, numbers):
  firstWinner = firstNum = lastWinner = lastNum = 0
  
  for num in numbers:
    for board in copy.copy(boards):
      if checkNum(board, num): #board got number
        if firstWinner == 0:    #if first winner
          firstWinner = board
          firstNum = num
        if len(boards) == 1:    #if last winner
          lastWinner = board
          lastNum = num
          return firstWinner, firstNum, lastWinner, lastNum
        boards.remove(board)

def calcResult(winner, winningNumber):
  sum = 0
  for row in winner:
    for n in row:
      if int(n) != -1:
        sum += int(n)
  return sum* int(winningNumber)

firstWinner, firstNum, lastWinner, lastNum = bingo(boards,numbers)
print("Part1:", calcResult(firstWinner, firstNum))
print("Part2:", calcResult(lastWinner, lastNum))

