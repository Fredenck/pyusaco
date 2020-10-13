def noDupli(s):
    return len(set(s))==len(s)
def change(order):
    nOrder = ""
    for i in range(1,len(order)-1):
        if order[i] == order[i+1] or order[i] == order[i-1]:#remove all consecutive "AA"
            pass
        else:
            nOrder += order[i]
    if order[-2] != order[-1]:
        nOrder += order[-1]
    if order[1] != order[0]:
        nOrder = order[0]+nOrder
    return nOrder
def noConsec(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1] or s[i] == s[i-1]:
            return False
    return True
#read in
fin = open ('circlecross.in', 'r')
fout = open ('circlecross.out', 'w')
order = fin.readline().strip()

nOrder = change(order)
while not noConsec(nOrder):
    nOrder = change(nOrder)
    print(nOrder)

count = 0
if nOrder == "":
    pass
else:
    flag = True
    startIdx = 0
    while flag:
        startVal = nOrder[startIdx]
        endIdx = nOrder[startIdx+1:].index(startVal)+startIdx+1
        section = nOrder[startIdx+1:endIdx]
        count += len(section)
        
        startIdx += 1+endIdx#Problem:ABCDCDAB, i just count 5 (5 between the 2 A's)
        #while it should be 2 because A and B cross and C and D cross, but A and C don't
        if noDupli(nOrder[startIdx:]):
            break
    

print(nOrder,order)
print(count)

fout.write (str(count) + '\n')
fout.close()