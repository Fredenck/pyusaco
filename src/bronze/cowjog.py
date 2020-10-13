#read in
fin = open ("cowjog.in", "r")
fout = open ("cowjog.out", "w")
N = int(fin.readline().strip())
spdList = []
for i in range(N):
    pos, speed = map(int, fin.readline().split())
    spdList.append(speed)
print(spdList)

spdList.reverse()
print(spdList)

group = 1
cur = spdList[0]
for i in range(len(spdList)-1):
    next = spdList[i+1]
    if cur>=next:
        group += 1
    if cur<next:#wait
        continue
    cur = spdList[i+1]
 
print(group)
fout.write (str(group) + "\n")
fout.close()