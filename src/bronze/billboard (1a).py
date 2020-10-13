def coverPart(x1,y1,x2,y2,x3,y3,x4,y4,area):
    if x3<x2<x4 and y4>=y2 and y3<=y1:#blocks right
        area -= abs((x2-x3)*(y2-y1))
    elif x3<x1<x4 and y4>=y2 and y3<=y1:#blocks left
        area -= abs((x4-x1)*(y2-y1))
    elif y3<y1<y4 and x4>=x2 and x3<=x1:#blocks bot
        area -=  abs((x2-x1)*(y4-y1))
    elif y3<y2<y4 and x3<x1 and x4>x2:#blocks top
        area -= abs((x2-x1)*(y2-y3))
    else:
        return False, area
    return True, area

fin1 = input()
fin2 = input()

x3,y3,x4,y4 = map(int, fin1.split(" "))#lawnmower
x1,y1,x2,y2 = map(int, fin2.split(" "))#feed

area = abs((x2-x1)*(y2-y1))
TF, area = coverPart(x1,y1,x2,y2,x3,y3,x4,y4,area)

if x4>x2 and y4>y2 and x3<x1 and y3<y1:#feed completely covers
    area = 0
elif TF:#covers part
    pass
else:#covers only a corner, or doesn't even cover
    pass

# print(area)
print(area)
