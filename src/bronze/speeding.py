#read in
fin = open ('speeding.in', 'r')
fout = open ('speeding.out', 'w')
N,M = map(int, fin.readline().split())

actual = [0]*101
bes = [0]*101

prev = 0
for i in range(N):
    dist,spd = map(int, fin.readline().split())
    for j in range(prev,prev+dist):
        actual[j] = spd
    prev += dist
prev = 0
for i in range(M):
    dist,spd = map(int, fin.readline().split())
    for j in range(prev,prev+dist):
        bes[j] = spd
    prev += dist

maxSpeed = 0
for i in range(100):
    if (bes[i]>actual[i]) and ((bes[i]-actual[i])>maxSpeed):#speeding and new max
        maxSpeed = bes[i]-actual[i]
        
print(actual)
print(bes)
print(maxSpeed)
fout.write (str(maxSpeed) + '\n')
fout.close()