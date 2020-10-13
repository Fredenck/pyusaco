def ct(line, xOrYList):# if only one cow is on one of the fences, then the area can be changed
    count = 0
    for i in xOrYList:
        if line == i:
            count += 1
        if count == 2:
            return False
    return True
# def min2(olist):#find the second least element
#     list = olist.copy()
#     idx = list.index(min(list))
#     list.remove(min(list))
#     return min(list)
# def max2(olist):
#     list = olist.copy()
#     list.remove(max(list))
#     return max(list)
def calcArea(oxList,oyList,toRemove):
    xList = oxList.copy()
    yList = oyList.copy()
    
    if toRemove == "L":
        idx = xList.index(min(xList))
    elif toRemove == "R":
        idx = xList.index(max(xList))
    elif toRemove == "T":
        idx = yList.index(max(yList))
    elif toRemove == "B":
        idx = yList.index(min(yList))
        
    del xList[idx]
    del yList[idx]
    
    return (max(xList)-min(xList))*(max(yList)-min(yList))
#read in
fin = open ('reduce.in', 'r')
fout = open ('reduce.out', 'w')
N = int(fin.readline().strip())
xList,yList = [],[]
for i in range(N):
    x,y = map(int, fin.readline().split())
    xList.append(x)
    yList.append(y)

area = (max(xList)-min(xList))*(max(yList)-min(yList))
if area != 0:
    posArea = [area]
    left = ct(min(xList),yList)
    right = ct(max(xList),yList)
    bot = ct(min(yList),xList)
    top = ct(max(yList),xList)
    if left:
        posArea.append(calcArea(xList,yList,"L"))
#         posArea.append((max(xList)-min2(xList))*(max(yList)-min(yList)))
    if right:
        posArea.append(calcArea(xList,yList,"R"))
#         posArea.append((max2(xList)-min(xList))*(max(yList)-min(yList)))
    if bot:
        posArea.append(calcArea(xList,yList,"B"))
#         posArea.append((max(xList)-min(xList))*(max(yList)-min2(yList)))
    if top:
        posArea.append(calcArea(xList,yList,"T"))
#         posArea.append((max(xList)-min(xList))*(max2(yList)-min(yList))) 
    print(area)       
    area = min(posArea)

print(area)
fout.write (str(area) + '\n')
fout.close()