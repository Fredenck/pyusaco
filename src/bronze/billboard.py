def areaOfRectangle(x1,y1,x2,y2):
    return (x2-x1)*(y2-y1)

def visibleArea(x1,y1,x2,y2,x3,y3,x4,y4):
    visible = areaOfRectangle(x1, y1, x2, y2)
    leftmostBlockedX = max(x1, x3)
    rightmostBlockedX = min(x2, x4)
    bottommostBlockedY = max(y1, y3)
    topmostBlockedY = min(y2, y4)
    if leftmostBlockedX < rightmostBlockedX and bottommostBlockedY < topmostBlockedY:
        visible -= areaOfRectangle(leftmostBlockedX, bottommostBlockedY, rightmostBlockedX, topmostBlockedY)
    return visible


    
    
fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')
x1,y1,x2,y2 = map(int, fin.readline().split())
x3,y3,x4,y4 = map(int, fin.readline().split())
x5,y5,x6,y6 = map(int, fin.readline().split())

totalArea = visibleArea(x1, y1, x2, y2, x5, y5, x6, y6) + visibleArea(x3, y3, x4, y4, x5, y5, x6, y6)

fout.write (str(totalArea) + '\n')
fout.close()