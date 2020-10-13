def prevSum(sensors,i,side):
    j=1
    while flag:
        sum += sensors[i-j][side]
        if j==i:
            return sum
        j+=1
        
#read in
fin = open ('traffic.in', 'r')
fout = open ('traffic.out', 'w')
N = int(fin.readline().strip())
sensors = []
for i in range(N):
    ramp,low,high = fin.readline().strip().split(" ")
    if ramp=='off':
        low = -1*low
        high = -1*high
    sensors.append([ramp,low,high])

prev = sensors[0]
sensor2 = sensors.copy()
for i in range(1,N):
    if sensors[i][0]==prev[0]:#same state then combine
        if prev[0]=='none':
            lower = max(sensors[i][1],prev[1])
            upper = min(sensors[i][2],prev[2])
        else:
            lower = sensors[i][1]+prev[1]
            upper = sensors[i][2]+sensors[2]

for i in range(N):#from left
    if sensors[i][0] == "none":
        lower = sensors[i][1]-prevSum(sensors,i,1)
        upper = sensors[i][2]-prevSum(sensors,i,2)

for i in range(N-1,-1,-1):#from the right
    if sensors[i]=="none":
        lower = sensors[i][1]-prevSum(sensors,i,1)
        upper = sensors[i][2]-prevSum(sensors, i, 2)

fout.write()
fout.close()