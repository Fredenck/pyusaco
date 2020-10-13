def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
fin = open ("marathon.in", "r")
fout = open ("marathon.out", "w")
N = int(fin.readline().strip())

coords = []
for i in range(N):
    x,y = map(int, fin.readline().split())
    coords.append([x,y])

oDist = 0
for i in range(len(coords)-1):
    oDist += dist(coords[i][0],coords[i][1],coords[i+1][0],coords[i+1][1])
print(oDist)

totalDists = []
for i in range(1,N-1):#first and last cannot be removed
    curDist = oDist
    toRemove = dist(coords[i][0],coords[i][1],coords[i-1][0],coords[i-1][1])
    toNext = dist(coords[i][0],coords[i][1],coords[i+1][0],coords[i+1][1])
    without = dist(coords[i-1][0],coords[i-1][1],coords[i+1][0],coords[i+1][1])
    curDist = curDist-(toRemove+toNext)+without
#     removeCoords = coords.copy()
#     removeCoords.remove(coords[i])
#     for j in range(len(removeCoords)-1):
#         curDist -= dist(removeCoords[j][0],removeCoords[j][1],removeCoords[j+1][0],removeCoords[j+1][1])
    totalDists.append(curDist)

print(totalDists)
fout.write (str(min(totalDists)) + "\n")
fout.close()