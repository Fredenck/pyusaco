def findmom(cow):
    for i in range(N):
        if cow == daughter[i]:
            return mother[i]
    return ""

def ancestor(cow1, cow2):
    count = 0
    while cow2 != "":
        if cow1 == cow2:
            return counter
        cow2 = findmom(cow2)
        count += 1
    return -1

def swap(one,two):
    temp = one
    one = two
    two = temp
    return one, two
    

fin = open ('family.in', 'r')
fout = open ('family.out', 'w')

N, bessie, elsie = fin.readline().split()
N = int(N)

ans = ''

mother = []
daughter = []
for i in range(N):
    mom,daught = fin.readline().split()
    mother.append(mom)
    daughter.append(daught)

cow = bessie
b = 0#bessie dist from ancestor
while cow != "":
    if(ancestor(cow, elsie) != 1):
        break
    cow = findmom(cow)
    b += 1
if cow == "":
    ans = "NOT RELATED"
a = ancestor(cow, elsie)#elsie dist from acestor
if a == 1 and b == 1:
    ans = "SIBLINGS"
elif a > 1 and b > 1:
    ans = "COUSINS"
else:
#     if a > b:
#         swap(elsie, bessie)
#         swap(a,b)
    if a > b:
        elsie, bessie = swap(elsie,bessie)
        a,b = swap(a,b)
        
    ans = elsie + " is the "
    for i in range(b-2):
        ans += "great-"
    if b > 1 and a == 0:
        ans += "grand-"
    if a == 0:
        ans += "mother"
    else:
        ans += "aunt"
    ans += " of " + bessie
        

print(ans)
fout.write (str(ans) + '\n')
fout.close()
