def main(N,row):
    equal = 0
    equal2 = 0
    #find bessie
    for i in range(N-1):
        if row[i] < row[i+1]:
            pass
        elif row[i] == row[i+1]:
            equal += 1
        else:
            bessie = row[i]
            besIdx = i
            break

    for i in range(N-2,-1,-1):
        if row[i] > row[i-1]:
            pass
        elif row[i] == row[i+1]:
            equal2 += 1
        else:
            bessie = row[i-1]
            besIdx = i-1
            break
    
    if row[besIdx]<= row[besIdx-1]:
        goFront = True
    else:
        goFront = False
    
    equal2 -= 1
    if not goFront:
        equal = equal2
    for i in range(N-1):
        if row[i]<bessie<= row[i+1] and i+1 != besIdx:
            ans = besIdx-i-equal
            return abs(ans)
        
fin = open ('outofplace.in', 'r')
fout = open ('outofplace.out', 'w')
N = int(fin.readline().strip())
row = []
for i in range(N):
    row.append(int(fin.readline().strip()))

test = sorted(row)
if test == row:
    ans = 0
else:
   ans = main(N,row)
    

# j = N
# for i in range(N-1,0,-1):#back to front
#     if row[i] == max(row[:j]):#if last one is the max of the list, with the list each time decreasing in size by 1
#         continue#correct place
# #     else:#correct

#     j -= 1
print(ans)
fout.write (str(ans) + '\n')
fout.close()
