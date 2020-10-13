def milkbad(i):
    for j in range(S):
        if (not personDrank(sick[j][0],i,sick[j][1])):
            return False
    return True

def personDrank(person,milk,time):
    for i in range(D):
        if (drink[i][0]==person) and (drink[i][1]==milk) and (drink[i][2]<time):
            return True
    return False

def peopleDrank(m):
    drank = [0]*51
    for i in range(D):
        if drink[i][1]==m:
            drank[drink[i][0]] = True
    
    num = 0
    for i in range(51):
        if drank[i]:
            num += 1
    return num
#read in
fin = open ('badmilk.in', 'r')
fout = open ('badmilk.out', 'w')
N,M,D,S = map(int, fin.readline().split())
drink = []
for i in range(D):
    p,m,t = map(int, fin.readline().split())
    drink.append([p,m,t])    
sick = []
for i in range(S):
    p,t = map(int, fin.readline().split())
    sick.append([p,t])

maxi = -1
for i in range(1,M+1):
    if milkbad(i):
        drank = peopleDrank(i)
        if drank>maxi:
            maxi = drank



print(maxi)
fout.write(str(maxi) + '\n')
fout.close()