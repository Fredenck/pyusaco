def passedTo(positions, i):#who each cow passes to
    lnum,rnum = -1,-1
    ldist,rdist = 1000,1000
    for j in range(len(positions)):
        if positions[j] < positions[i] and (positions[i]-positions[j]) < ldist:
            lnum = j
            ldist = positions[i]-positions[j]
    for k in range(len(positions)):
        if positions[k] > positions[i] and (positions[k]-positions[i]) < rdist:
            rnum = k
            rdist = positions[k]-positions[i]
    if ldist<=rdist:
        return lnum
    return rnum

#read in
fin = open ('hoofball.in', 'r')
fout = open ('hoofball.out', 'w')
cows = int(fin.readline().strip())
positions = list(map(int, fin.readline().split(" ")))
ans = 0
key = cows*[0]
for i in range(cows):
    key[passedTo(positions, i)] += 1

print(sorted(positions))
for i in range(cows):
    if key[i] == 0:
        ans += 1
    if i<passedTo(positions, i) and passedTo(positions, passedTo(positions, i)) == i and key[i] == 1 and key[passedTo(positions, i)] == 1:
        ans+=1
print(ans)
fout.write (str(ans) + '\n')
fout.close()