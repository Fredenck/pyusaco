def sameMilk(j,used,sick):
    if j not in used:
        used.append(j)
    for k in range(len(drink)):
        for j in sick:
            if (i[:2]==drink[k][:2]) and (i[2]<j[1]) and(i[2] != drink[k][1]):#same person/same milk,
                return False
    return True
                
def countOccurance(drink,ele):
    count = 0
    for i in drink:
        if ele == i[1]:
            count += 1
    return count
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

used = []
# for j in drink:
#     if j 

posSick = []
for i in sick:
    person = i[0]
    timeSick = i[1]
    
    for j in drink:        
        if (j[0] == person) and (j[2]<timeSick) and (not (sameMilk(j,used,sick))):
            posSick.append(j[1])
            print(j)

# for i in posSick:
#     if (i not in used):
#         used.append(i)
#         flag = True
#     if flag and (not (sameMilk(i,drink,sick))):
#         del used[-1]
#         flag = False
        
print(len(used),used)

realPosSick = []
for i in list(set(posSick)):
    if posSick.count(i) == len(sick):
        realPosSick.append(i)

maximum = 0
for i in realPosSick:
    ct = countOccurance(drink,i)
    if ct > maximum:
        maximum = ct
        
    
# print(drink)
# print(sick)
print(maximum)
fout.write(str(maximum) + '\n')
fout.close()