def ifremove(order):
    for i in range(len(order)):
        copy = order.copy()
        if copy == sorted(copy):
            return -1,True
        del copy[i]
        if copy == sorted(copy):
            return i,True
    return 0,False
#read in
fin = open ('sleepy.in', 'r')
fout = open ('sleepy.out', 'w')
N = int(fin.readline().strip())
order = list(map(int, fin.readline().split()))
cor = sorted(order)

steps = N-1
idx,tf = ifremove(order)
if tf:#in order besides one
    steps = idx+1
elif cor == order.reverse():#backwards
    steps = N-1
else:
    steps = 0
    for i in range(len(order)-1):
        if abs(order[i]-order[i+1])>= 2:
            steps += abs(order[i]-order[i+1])-1
if steps>N-1:
    steps = N-1

print(steps)
fout.write (str(steps) + '\n')
fout.close()