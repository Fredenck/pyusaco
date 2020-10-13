def isBetween(s,e,y):
    larger = max(s,e)
    smaller = min(s,e)
    return smaller<=y<=larger
    
#read in
fin = open ('lostcow.in', 'r')
fout = open ('lostcow.out', 'w')
x,y = map(int, fin.readline().split())

notFound = True
rate = 1
total = 0
count = 0
r = 1
s = x
e = x
while notFound:
    if count % 2 == 0:
        e = x+rate
    else:
        e = x-rate
    
    if isBetween(s,e,y):        
        notFound = False
        
    s = e
    total = r
    r = 2*r + 2
    rate *= 2
    count += 1

total = total-abs(e-y)
print(total)
fout.write (str(total) + '\n')
fout.close()