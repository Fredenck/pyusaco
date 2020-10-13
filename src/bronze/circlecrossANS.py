def singles(orderNum,greaterThan,first,last):
    count = 0
    appearances = [0]*26
    for i in range(first+1,last):
        appearances[orderNum[i]] += 1
    
    for i in range(greaterThan+1,len(appearances)):
        if appearances[i] == 1:
            count += 1
    return count
    
#read in
fin = open ('circlecross.in', 'r')
fout = open ('circlecross.out', 'w')
order = fin.readline().strip()

orderNum = []
for i in range(len(order)):
    orderNum.append(ord(order[i])-ord("A"))
    
count = 0

for i in range(26):
    first = orderNum.index(i)#first occurrence
    last = orderNum.index(i,first+1)#last occurrence
    
    count += singles(orderNum, i, first, last)
    
print(count)
fout.write (str(count) + '\n')
fout.close()