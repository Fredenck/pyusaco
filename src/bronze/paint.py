#read in
fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
a,b = map(int, fin.readline().split())
c,d = map(int, fin.readline().split())

tot = 0
for i in range(100):
    if i>=a and (i+1)<=b:
        tot += 1
    elif i>=c and (i+1)<=d:
        tot += 1
print(tot)

fout.write (str(tot) + '\n')
fout.close()