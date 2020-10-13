def color(c):
    for i in range(N):
        for j in range(N):
            if final[i][j] == c:
                return True
    return False

def above(c1,c2):
    top,left,bot,right = N,N,0,0
    for i in range(N):
        for j in range(N):
            if final[i][j] == c2:
                top = min(top, i)
                bot = max(bot, i)
                left = min(left, j)
                right = max(right, j)
    
    for i in range(top,bot+1):
        for j in range(left,right+1):
            if final[i][j] == c1:
                return True
    return False
#read in
fin = open ('art.in', 'r')
fout = open ('art.out', 'w')
N = int(fin.readline().strip())
final = []
for i in range(N):
    row = list(map(int,list(fin.readline().strip())))
    final.append(row)

count = 0
for i in range(1,10):
    if color(i):
        flag = True
        for j in range(1,10):
            if j!=i and color(j) and above(i,j):
                flag = False
        if flag:
            count += 1

print(count)
fout.write (str(count) + '\n')
fout.close()