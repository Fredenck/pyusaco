def find(a,factory,count):
    for i in range(len(factory)):
        if a==factory[i][1]:
            try:
                count += find(factory[i][0],factory,count)-count
            except RecursionError as re:#if 1->6, 6->2, 2->1 (infinite loop will cause error)
                return -1000
    return count+1
with open ('factory.in', 'r') as fin:
    N = int(fin.readline().strip())
    factory = []
    ans = -1
    for i in range(N-1):
        factory.append(list(map(int, fin.readline().split())))
rec = -1
for i in factory:
    if rec!=i[1]:
        count = 0
    give=i[0]
    rec=i[1]
    count += find(rec,factory,count)-1#count how many things lead up to rec
    if count>=N-1:
        ans = rec
        print(count)
        break
    if count<0:
        break
    ans = -1
for j in range(101):
    for i in range(len(factory)):
        if factory[i][0]==ans:
            ans = factory[i][1]
print(ans)
print(count)
with open ('factory.out', 'w') as fout:        
#     if N==100:
#         ans = -1
    fout.write(str(ans) + '\n')
    fout.close()