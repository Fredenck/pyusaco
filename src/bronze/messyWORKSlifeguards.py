fin = open ('lifeguards.in', 'r')
fout = open ('lifeguards.out', 'w')
N = int(fin.readline().strip())
shiftTimes = []
for i in range(N):
    x,y = map(int, fin.readline().split())
    shiftTimes.append([x,y])

shiftTimes = sorted(shiftTimes, key=lambda x: x[0])#gotten from https://stackoverflow.com/questions/36955553/python-sorting-list-of-lists-by-the-first-element-of-each-sub-list?rq=1

pos = [0]*N
for i in range(N-1):
    service = shiftTimes[i][1]-shiftTimes[i][0]
    if shiftTimes[i+1][0]<shiftTimes[i][1]:#overlap
        overlap = shiftTimes[i][1]-shiftTimes[i+1][0]#overlap
        pos[i] += service - overlap 
        pos[i+1] -= overlap
    else:
        pos[i] += service
pos[i+1] += shiftTimes[i+1][1]-shiftTimes[i+1][0]

worst = min(pos)
idx = pos.index(worst)
del shiftTimes[idx]#fire the worst

overlap = 0
for i in range(N-2):
    service = shiftTimes[i][1]-shiftTimes[i][0]
    if shiftTimes[i+1][0]<shiftTimes[i][1]:#overlap
        overlap -= shiftTimes[i][1]-shiftTimes[i+1][0]#overlap
    
#delete 2 overlaps from the one worker(overlap before and after equals 2 overlaps)

time = 0
for i in shiftTimes:
    time += i[1]-i[0]

time += overlap#overlaps is negative

# print(time)
fout.write (str(time) + '\n')
fout.close()
