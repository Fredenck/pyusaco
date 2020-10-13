#read in
fin = open ("learning.in", "r")
fout = open ("learning.out", "w")
N,A,B = map(int,fin.readline().strip().split())
spots,weights,total = [],[],[]
for i in range(N):
    posSpot, W = fin.readline().split()
    total.append([int(W),posSpot])
total.sort()
print(total)
d= 0
metB,metA = False,False

for i in range(N-1):
    if (total[i][0]<=A) and (total[i+1][0]>=A):
        metA = True
        
        if (total[i][1]=="S" and total[i+1][1]=="NS") or (total[i][1]=="NS" and total[i+1][1]=="S"):
            M = (total[i+1][0]-total[i][0])/2
            M = int(M+0.5)
            d += M
        
        elif total[i][1]=="S" and total[i+1][1]=="S":
            d += total[i+1][1]-total[i][1]
    
    if metA:
        if metB:
            break
        
        if (total[i][0]<=B) and (total[i+1][0]>=B) and (total[i][1]=="S"):
            total[i][0]=B
            metB = True
        
        if (total[i][1]=="S" and total[i+1][1]=="NS") or (total[i][1]=="NS" and total[i+1][1]=="S"):
            d += (total[i+1][0]-total[i][0])/2
            d = int(d+0.5)
        
        if total[i][1]=="S" and total[i+1][1]=="S":
            d += total[i+1][1]-total[i][1]

print(d)
fout.write (str() + "\n")
fout.close()