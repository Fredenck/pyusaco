def ct(x,y,xVal,yVal):
    BL,BR,TL,TR = 0,0,0,0
    for i in range(len(xVal)):
            if (xVal[i]<x) and (yVal[i]<y):
                BL += 1
            elif (xVal[i]>x) and (yVal[i]<y):
                BR += 1
            elif (xVal[i]<x) and (yVal[i]>y):
                TL += 1
            elif (xVal[i]>x) and (yVal[i]>y):
                TR += 1
    return max(BL,BR,TL,TR)
#read in
fin = open ('balancing.in', 'r')
fout = open ('balancing.out', 'w')
N, B = map(int, fin.readline().split())
xVal = []
yVal = []
posA = []
posB = []
for i in range(N):
    x,y = map(int, fin.readline().split())
    if (x+1 not in posA):#we don't want duplicates
        posA.append(x+1)
    if (y+1 not in posB):
        posB.append(y+1)
    xVal.append(x)
    yVal.append(y)
posA = sorted(posA)
posB = sorted(posB)
del posA[-1]#the last one would be one right to the farthest right cow, which is not needed
del posB[-1]
print(posA,posB)

M = 1000000000
for i in range(len(posA)):
    for j in range(len(posB)):#loop through all possible values of a and b
        posM = ct(posA[i],posB[j],xVal,yVal)#find the maximum in each section 
        if posM<M:
            M = posM
print(M)

fout.write (str(M) + '\n')
fout.close()