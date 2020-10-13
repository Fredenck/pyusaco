def B2A(A,B):
    Bcopy = B.copy()
    A2 = A.copy()
    B2 = B.copy()
    alist,blist = [],[]
    newlist = []
    for i in Bcopy:
        A2.append(i)
        B2.remove(i)
        newlist.append((A2, B2))
       # alist.append(A2)
       # blist.append(B2)
        
        A2 = A.copy()
        B2 = B.copy()
#     newlist = list(set(newlist))
#     alist = [list(x) for x in set(tuple(x) for x in alist)]
#     blist = [list(x) for x in set(tuple(x) for x in blist)]
    newlist = [list(x) for x in set(x for x in newlist)]
    
    return newlist

def movement1(firstList,secondList):
    fcopy = firstList.copy()
    scopy = secondList.copy()
    posList1, posList2 = [],[]
    totalSet = set()
    
    #Tuesday
    newlist = B2A(scopy, fcopy)
    print(newlist)
    
    newlist2 = []
    for i in range(len(newlist)):
        nl = B2A(newlist[i][0], newlist[i][1])
        newlist2.extend(nl)
    print(newlist2)
    
        
    
    return posList1, posList2, totalSet



fin = open ('backforth.in', 'r')
fout = open ('backforth.out', 'w')
first = list(map(int, fin.readline().strip().split(" ")))
second = list(map(int, fin.readline().strip().split(" ")))

total = 1000

posList1, posList2, totalSet = movement1(first, second)


# print(posList)
# print(B2A([1,1,1,3], [2,2,2,2,2]))
fout.write (str() + '\n')
fout.close()
