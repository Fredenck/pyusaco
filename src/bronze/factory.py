def find(a,factory,count,prevList):
    for i in range(len(factory)):
        if factory[i] in prevList:
            break
        if a==factory[i][1]:
            prevList.append(factory[i])
            count += find(factory[i][0],factory,count,prevList)
    return count
with open ('factory.in', 'r') as fin:
    N = int(fin.readline().strip())
    factory = []
    ans = -1
    for i in range(N-1):
        x = list(map(int, fin.readline().split()))
        if x not in factory:
            factory.append(x)
N = len(factory)-1
rec = -1
for i in factory:
    if rec!=i[1]:
        count = 1
    give=i[0]
    rec=i[1]
    prevList = []
    count += find(rec,factory,count,prevList)
    if count>=N-1:
        ans = rec
        break
for j in range(101):
    for i in range(len(factory)):
        if factory[i][0]==ans:
            ans = factory[i][1]
print(ans)
with open ('factory.out', 'w') as fout:
    fout.write(str(ans) + '\n')
    fout.close()