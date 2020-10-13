def check(A,B,curOrder):
    if (A in curOrder) and (B in curOrder):
        if curOrder.index(A)<=curOrder.index(B):
            return True
        else:
            return False
fin = open ("cowroute.in", "r")
fout = open ("cowroute.out", "w")
A,B,N = map(int, fin.readline().split())
costPlusFlights = []
for i in range(N):
    cost,citiesAmnt = map(int, fin.readline().split())
    order = list(map(int,fin.readline().split()))
    costPlusFlights.append([cost,order])

print(A,B,N)
print(costPlusFlights)
costPlusFlights.sort()
print(costPlusFlights)

posCost = []
for i in range(N):
    cur = costPlusFlights[i][1]
    minCost = 0
    
    if (A in cur) and (A != cur[-1]):
        idx = cur.index(A)
        posB = cur[idx+1:]
        minCost = costPlusFlights[i][0]
        
        newCostFlights = costPlusFlights.copy()
        newCostFlights.remove(costPlusFlights[i])
        for j in range(len(newCostFlights)):
            c2 = newCostFlights[j][1]
            for k in posB:
                if check(k, B, c2):
                    minCost += newCostFlights[j][0]
                    posCost.append(minCost)
print(posCost)
# posCost = []
# for i in range(len(costPlusFlights)):
#     curOrder = costPlusFlights[i][1]
#     if check(A,B,curOrder):
#         posCost.append(costPlusFlights[i][0])

# print(posCost)
# if len(posCost)==0:
#     posCost.append(-1)
fout.write (str(min(posCost)) + "\n")
fout.close()