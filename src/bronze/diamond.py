def NInRange(weights,range):
    ct = 0
    for i in weights:
        if range[0]<=i<=range[1]:
            ct += 1
    return ct
    
fin = open ("diamond.in", "r")
fout = open ("diamond.out", "w")
N,K = map(int, fin.readline().split())

weights = []
for i in range(N):
    weights.append(int(fin.readline().strip()))

okRanges = []
for i in weights:
    okRanges.append([i-K,i])
    okRanges.append([i,i+K])

maxPos = -1
for i in okRanges:
    amount = NInRange(weights,i)
    if amount>maxPos:
        maxPos = amount
print(maxPos)



fout.write (str(maxPos) + "\n")
fout.close()