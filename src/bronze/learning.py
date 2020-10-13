#read in
fin = open ("learning.in", "r")
fout = open ("learning.out", "w")
N,A,B = map(int,fin.readline().strip().split())
spots,weights,total = [],[],[]
for i in range(N):
    posSpot, W = fin.readline().split()
#     spots.append(posSpot)
#     weights.append(int(W))
    total.append([int(W),posSpot])
total.sort()

spotRanges = []
Nbot = 1
g = True
for i in range(N-1):
    if g:
        bot = Nbot
    if (total[i][1]=="S"):
        sum = total[i][0]+total[i+1][0]
        if sum%2==0:
            top,Nbot = int(sum/2),int(sum/2)
        else:
            top = int(sum/2)
            Nbot = int(sum/2)+1
        spotRanges.append([bot,top])
        g = True
    else:
        g = False
        sum = (total[i][0]+total[i+1][0])
        if sum%2==1:
            bot = int(sum/2)+1
        else:
            bot = int(sum/2)
if B>Nbot:
    sum = total[-2][0]+total[-1][0]
    if sum%2==0:
        spotRanges.append([int(sum/2), B])
    else:
        spotRanges.append([int(sum/2)+1, B])

print(spotRanges)

ct = 0
f = False
for i in range(len(spotRanges)):
    if i < len(spotRanges)-1:
        if spotRanges[i][1]==spotRanges[i+1][0]:
            ct -= 1
    if spotRanges[i][0]<=A<=spotRanges[i][1]:
        ct += spotRanges[i][1]-A+1
    elif spotRanges[i][0]>A:
        f = True
    if f:
        if spotRanges[i][1]<=B:
            ct += spotRanges[i][1]-spotRanges[i][0]+1
        else:
            ct += B-spotRanges[i][0]+1
print(A,B)
print(ct)

fout.write (str(ct) + "\n")
fout.close()