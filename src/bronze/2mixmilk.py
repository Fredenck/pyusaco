fin = open ('mixmilk.in', 'r')
fout = open ('mixmilk.out', 'w')
c1,m1 = map(int,fin.readline().split())
c2,m2 = map(int,fin.readline().split())
c3,m3 = map(int,fin.readline().split())

for i in range(0,100):
    if i%3==0:
        if m2+m1<=c2:
            m2 += m1
            m1 = 0
        else:
            need = c2-m2
            m2 += need
            m1 -= need
    if i%3==1:
        if m3+m2<=c3:
            m3 += m2
            m2 = 0
        else:
            need = c3-m3
            m3 += need
            m2 -= need
    if i%3==2:
        if m1+m3<=c1:
            m1 += m3
            m3 = 0
        else:
            need = c1-m1
            m1 += need
            m3 -= need        
print(m1,m2,m3)

fout.write(str(m1)+"\n"+str(m2)+"\n"+str(m3))
fout.close()