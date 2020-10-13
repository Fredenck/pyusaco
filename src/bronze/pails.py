#read in
fin = open ('pails.in', 'r')
fout = open ('pails.out', 'w')
X,Y,M = map(int, fin.readline().split())
largest = -1
for i in range(int(M/X)+1):
    for j in range(int(M/Y)+1):
        if largest<(X*i+j*Y)<= M:
            largest = X*i+j*Y
            

print(largest)
fout.write (str(largest) + '\n')
fout.close()