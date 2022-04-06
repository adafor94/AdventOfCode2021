x_min, x_max = 211, 232
y_min, y_max = -124, -69

def testTrajectory(xVel, yVel, x=0, y=0):
    #We are to far to the right or below target area
    if x > x_max or y < y_min: 
        return 0

    #We are within the target area
    if x >= x_min and y <= y_max: 
        return 1
    
    #Else try next step
    x = x+xVel
    y = y+yVel
    xVel -= xVel > 0
    yVel -= 1
   
    return testTrajectory(xVel, yVel, x, y)

possibleVelocitites = [(x,y) for x in range(1,x_max+1) for y in range(y_min, -y_min)]
hits = [testTrajectory(xVel, yVel) for xVel, yVel in possibleVelocitites]

part1 = sum(range(0,abs(y_min)))
print("Part1:", part1)
print("Part2:", sum(hits))

