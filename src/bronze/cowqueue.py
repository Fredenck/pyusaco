def shorten(akey):
    nkey = []
    for i in range(N-1):
        end = akey[i][0]+akey[i][1]
        part = [akey[i][0],akey[i][1]]
        if end>akey[i+1][0]:#overlap
            change = end-akey[i+1][0]
            for j in range(i+1,len(akey)):
                if akey[j][0]<(akey[j-1][0]+akey[j-1][1]):
                    akey[j][0] = akey[j-1][0]+akey[j-1][1]
    return akey
#read in
fin = open ('cowqueue.in', 'r')
fout = open ('cowqueue.out', 'w')
N = int(fin.readline().strip())

key = []
for i in range(N):
    s,req = map(int, fin.readline().split())
    key.append([s,req])
    

time = 0
if N == 1:
    time = key[0][0]+key[0][1]
    over = True
    
else:
    key = sorted(key, key=lambda x: x[0])#sort by first val
    key = shorten(key)

    
print(key,sum(key[-1]))
#code


fout.write (str(sum(key[-1])) + '\n')
fout.close()