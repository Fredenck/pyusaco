#read in input
fin = open ('blist.in', 'r')
fout = open ('blist.out', 'w')
N = int(fin.readline().strip())
# start = []
# end = []
# bucketsNeeded = []
# for i in range(N):
#     s,e,b = map(int, fin.readline().split())
#     start.append(s)
#     end.append(e)
#     bucketsNeeded.append(b)
total = []
for i in range(N):
    s,e,b = map(int, fin.readline().split())
    total.append([s,e,b])

#sort by first val
total = sorted(total, key=lambda x: x[0])#gotten from https://stackoverflow.com/questions/36955553/python-sorting-list-of-lists-by-the-first-element-of-each-sub-list?rq=1

buckets = total[0][2]
q = 0
lowestEnd = total[q][1]
lowestCorBuckets = total[q][2]
for i in range(1, N):
    avail = total[i-1][2]
    if total[i][0] < total[i-1][1]:#overlap with prev
        avail -= total[i-1][2]#cannot use 2 at once
        buckets += total[i][2]
    else:#no overlap
        if total[i][2] > buckets:
            need = total[i][2]-buckets
            buckets += need
            avail -= need
            
    
    if lowestEnd <= total[i][0] and q+1 != i :#if the old ones free up space for new ones
        avail += lowestCorBuckets
        q += 1
        lowestEnd = total[q][1]
        lowestCorBuckets = total[q][2]
    buckets -= avail
    
        
    
    

# print(buckets)

fout.write (str(buckets) + '\n')
fout.close()
