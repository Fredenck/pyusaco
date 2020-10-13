fin = open ('outofplace.in', 'r')
fout = open ('outofplace.out', 'w')
N = int(fin.readline().strip())
row = []
for i in range(N):
    row.append(int(fin.readline().strip()))

test = sorted(row)
swaps = -1

if test == row:
    ans = 0
else:
    for a in range(N):
        if test[a] != row[a]:
            swaps += 1
    swaps = max(0,swaps)
    

print(swaps)
fout.write (str(swaps) + '\n')
fout.close()
