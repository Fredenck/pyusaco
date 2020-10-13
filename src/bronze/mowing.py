#read in
fin = open ('mowing.in', 'r')
fout = open ('mowing.out', 'w')
N = int(fin.readline().strip())
dirList,distList = [],[]
for i in range(N):
    dir,dist = fin.readline().split()
    distList.append(int(dist))#[10,2,3...]
    dirList.append(dir)#["N","E"...]

size = 1000
MP = max(distList)
# MP = int((size/2)-0.5)#5/2=2.5; 2.5=>2 since 2 is the 3rd element, and 3 is the MP of 1,2,3,4,5
#from https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
farm = [[-1 for x in range(size)] for y in range(size)]#creates a list of lists full of -1, to represetn his farm
t=0
growth = []
x,y = MP,MP
# farm[MP][MP] = 0
try:
    for i in range(N):
        for j in range(1,distList[i]+1):
            t += 1
            if dirList[i] == "N":
                if farm[x-j][y] != -1:
                    growth.append(t-farm[x-j][y])
                farm[x-j][y] = t
            elif dirList[i] == "S":
                if farm[x+j][y] != -1:
                    growth.append(t-farm[x+j][y])
                farm[x+j][y] = t
            elif dirList[i] == "E":
                if farm[x][y+j] != -1:
                    growth.append(t-farm[x][y+j])
                farm[x][y+j] = t
            elif dirList[i] == "W":
                if farm[x][y-j] != -1:
                    growth.append(t-farm[x][y-j])
                farm[x][y-j] = t
        if dirList[i] == "N":
            x -= distList[i]
        elif dirList[i] == "E":
            y += distList[i]
        elif dirList[i] == "S":
            x += distList[i]
        elif dirList[i] == "W":
            y -= distList[i]

except:
#     print(farm)
    if len(growth)==0:
        growth.append(-1)
    if min(growth)==1001:
        growth.append(-1)
    print(min(growth))
    fout.write (str(min(growth)) + '\n')
    fout.close()
else:
#     print(farm)
    if len(growth)==0:
        growth.append(-1)
    if min(growth)==1001:
        growth.append(-1)
    print(min(growth))
    fout.write (str(min(growth)) + '\n')
    fout.close()
    