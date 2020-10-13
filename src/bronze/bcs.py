def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
def ct(piece):
    amnt = 0
    for i in piece:
        amnt += i[0].count("#")
        if amnt > N*N:
            break
        print(amnt)
    return amnt
#read in
fin = open ('bcs.in', 'r')
fout = open ('bcs.out', 'w')
N,K = map(int, fin.readline().split())
orig = []
for i in range(N):
    orig.append([fin.readline().strip()])
    
pieces = []
for i in range(K):
    part = []
    for j in range(N):
        part.append([fin.readline().strip()])
    if ct(part)<ct(orig):
        pieces.append(part+[i+1])
        
print(orig)
print(pieces)

if len(pieces)==2:
    p1,p2 = pieces[0][-1],pieces[1][-1]
else:
    for i in pieces:
        TB = 0
        for j in range(N):
            if i[j] == "."*N:
                TB += 1
            else:
                break
            
        for j in range(TB):
            mid = i[j][j:]+[N*"."]    

fout.write (str(p1) + " "+str(p2)+'\n')
fout.close()