def check(cur, usedSet):#if any element of cur is in usedSet
    for i in cur:
        if i in usedSet:
            return True
    return False
def com(cur,usedSet):#returns all shared calues
    return list(usedSet.intersection(cur))
def findPlant(common, pastures,toBePlanted,SKIP):
    seed = []
    for i in common:
        ct = 0
        for j in pastures:
            if j == SKIP:
                ct += 1
                continue
            
            if i in j:
                seed.append(toBePlanted[ct])
                break
            ct += 1
    
    return max(seed)+1
#read in
fin = open ('revegetate.in', 'r')
fout = open ('revegetate.out', 'w')
N,M = map(int, fin.readline().split())
pastures = []#which cows(values) like which pasture(index)
for i in range(N):
    pastures.append([])
for i in range(1,M+1):
    index1, index2 = map(int, fin.readline().split())
    pastures[index1-1].append(i)
    pastures[index2-1].append(i)

toBePlanted = [1]*N
usedSet = set()
usedSet.update(pastures[0])
for i in range(1,N):
    cur = pastures[i]
    if check(cur,usedSet):#if any element of cur is in usedSet
        common = com(cur, usedSet)
        
        plant = findPlant(common, pastures, toBePlanted,cur)
        
        toBePlanted[i] = plant
    usedSet.update(cur)

print(pastures)
print(toBePlanted)

# toBePlanted = list(set(map(str, toBePlanted)))#convert all elements in toBePlanted to str
toBePlanted = [str(i) for i in toBePlanted]

fout.write (''.join(toBePlanted) + '\n')
fout.close()