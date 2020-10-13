import itertools
import time
t0 = time.time()
def summing(alist):#check if a digit carries over
    if sum(alist)>=10:
        return False
    return True

fin = open ('escape.in', 'r')
fout = open ('escape.out', 'w')
N = int(fin.readline().strip())
cows = []
for i in range(N):
    cows.append(int(fin.readline().strip()))

t1 = time.time()
subsets = []#all combinations from the list of len2 to N
for i in range(2,N+1):
    for j in itertools.combinations(cows, i):
        subsets.append(j)
t2 = time.time()
subsets.reverse()
t3 = time.time()
# print(cows)
# print(subsets)

pos = []
f  = True
for i in subsets:
    for j in range(1,len(str(max(i)))+1):#ones, tens, hundreds...
        alist = []
        for k in i:
            if j>len(str(k)):
                continue
            alist.append(int(str(k)[-j]))
        if not (summing(alist)):#if it carries over
            f = False
            break
        else:
            f = True
    if f:
        pos = len(i)
        break
t4 = time.time()
print(pos)
print(t1-t0,t2-t1,t3-t2,t4-t3,t4-t0)
print()
fout.write (str(pos) + '\n')
fout.close()