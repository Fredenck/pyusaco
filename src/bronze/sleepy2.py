#read in
fin = open ('sleepy.in', 'r')
fout = open ('sleepy.out', 'w')
N = int(fin.readline().strip())
order = list(map(int, fin.readline().split()))

count = 1
for i in range(N-1,0,-1):#back to front
    if order[i] > order[i-1]:
        count += 1
    else:
        break
steps = N-count

print(steps,count)
fout.write (str(steps) + '\n')
fout.close()