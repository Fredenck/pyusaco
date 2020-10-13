fin = open ('shuffle.in', 'r')
fout = open ('shuffle.out', 'w')
N = int(fin.readline().strip())
order = list(map(int, fin.readline().strip().split(" ")))
final = list(map(int,fin.readline().split(" ")))+[0]
ans = ''

moveTo = [0]*(N) 
for i in range(N):
    moveTo[order[i]-1] = i+1

orig = [0]*(N+1)
# for i in range(1,N+1):
for j in range(3):
    for i in range(N):
        cur = moveTo[i]
        if j == 0:
            orig[cur-1] = final[i]
        else:
            orig[cur-1] = copies[i]
    copies = orig.copy()
    
for i in range(N):
    ans += str(orig[i])+'\n'
print(ans)
fout.write (str(ans))
fout.close()