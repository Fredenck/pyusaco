#read in
fin = open ('revegetate.in', 'r')
fout = open ('revegetate.out', 'w')
N,M = map(int, fin.readline().split())
notequal = []
for i in range(1,M+1):
    index1, index2 = map(int, fin.readline().split())
    notequal.append([index1-1,index2-1])
    

for i in notequal:
    i.sort()
print(notequal)
# s = sorted(s, key = lambda x: (x[1], x[2]))
# notequal = sorted(notequal, key=lambda x: (x[0],x[1]))
print(notequal)

# q="1"*N
# for i in notequal:
#     if q[i[0]]==q[i[1]]:
#         listq = list(q)
#         listq[i[1]] = str(int(q[i[0]])+1)
#         q=''.join(listq)
# print(q)
q = [1]*N
for i in range(N):#position index
    for g in range(1,5):#possible
        ok = True
        for j in notequal:
            if (j[1]==i) and (q[j[0]]==g):#cur pos is larger of the 2 and feed at the smaller pos is g
                ok = False#go to next g
                break
        if ok:#found a g
            break
    q[i]=g
    print(g)
fout.write (str(i) + '\n')
fout.close()