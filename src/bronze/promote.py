#read in
fin = open ('promote.in', 'r')
fout = open ('promote.out', 'w')
b1,b2 = map(int, fin.readline().split())
s1,s2 = map(int, fin.readline().split())
g1,g2 = map(int, fin.readline().split())
p1,p2 = map(int, fin.readline().split())

bs,sg,gp = 0,0,0

pdif = p2-p1
bs += pdif
sg += pdif
gp += pdif

gdif = g2-g1
bs += gdif
sg += gdif

sdif = s2-s1
bs += sdif

print(bs,sg,gp)
fout.write (str(bs) + '\n' + str(sg) + '\n' + str(gp) + '\n')
fout.close()