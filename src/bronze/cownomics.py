def unique(spotted,plain):
    s = set(spotted)
    p = set(plain)
    
    if (s&p):
        return False
    return True
#read in
fin = open ('cownomics.in', 'r')
fout = open ('cownomics.out', 'w')
N,M = map(int, fin.readline().split())
spotted,plain = [],[]

for i in range(N):
    spotted.append(fin.readline().strip())
for i in range(N):
    plain.append(fin.readline().strip())

count = 0
help1,help2 = [],[]
for i in range(M):
    for j in spotted:
        help1.append(j[i])
    for j in plain:
        help2.append(j[i])
    
    if unique(help1,help2):
        count += 1 
    
    help1,help2 = [],[]

print(count)
fout.write (str(count) + '\n')
fout.close()