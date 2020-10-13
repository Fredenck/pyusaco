#read in input
fin = open ('blist.in', 'r')
fout = open ('blist.out', 'w')
N = int(fin.readline().strip())
buckets = []
starts = []
ends = []
for i in range(N):
    s,e,b = map(int, fin.readline().split())
    buckets.append([s,b])
    buckets.append([e,(b*-1)])

buckets = sorted(buckets, key=lambda x: x[0])#gotten from https://stackoverflow.com/questions/36955553/python-sorting-list-of-lists-by-the-first-element-of-each-sub-list?rq=1

req = 0
maxBuckets = -1
for i in buckets:
    req += i[1]
    if req > maxBuckets:
        maxBuckets = req
    


print(maxBuckets)

fout.write (str(maxBuckets) + '\n')
fout.close()
