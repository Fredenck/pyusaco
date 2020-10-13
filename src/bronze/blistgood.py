#read in input
fin = open ('blist.in', 'r')
fout = open ('blist.out', 'w')
N = int(fin.readline().strip())
buckets = []
starts = []
ends = []
for i in range(N):
    s,e,b = map(int, fin.readline().split())
    starts.append(s)
    ends.append(e)
    buckets.append(b)
    
req = 0
a = 0
maxBuckets = 0
for j in range(1000):
    for i in range(N):
        if j == starts[i]:
            req += buckets[i]
        if j == ends[i]:
            req -= buckets[i]
    if maxBuckets<req:
        maxBuckets = req
    


print(maxBuckets)

fout.write (str(maxBuckets) + '\n')
fout.close()
