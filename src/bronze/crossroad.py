#read in
fin = open ('crossroad.in', 'r')
fout = open ('crossroad.out', 'w')
N = int(fin.readline().strip())
all = []
for i in range(N):
    id,side = map(int, fin.readline().split())
    all.append([id,side])
curSides = [-1]*10#sides each cow is currently on--each cow is each value(curSides[0] is cow ID1)
count = 0
for i in all:
    id = i[0]-1
    if curSides[id] == -1:
        curSides[id] = i[1]
    else:
        if curSides[id] == i[1]:
            pass
        else:
            curSides[id] = i[1]
            count += 1
    

print(count)
fout.write (str(count) + '\n')
fout.close()