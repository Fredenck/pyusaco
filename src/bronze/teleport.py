#read in
fin = open ('teleport.in', 'r')
fout = open ('teleport.out', 'w')
a,b,x,y = map(int, fin.readline().split())

#Case1: Without teleporter

dist1 = abs(b-a)

#Case2: With teleporter

#Case2a: teleport from x to y
dist2a = abs(a-x)#get to teleport start
dist2a += abs(b-y)#get from teleport end to destination

#Case2b: teleport from y to x
dist2b = abs(a-y)
dist2b += abs(b-x)

ans = min(dist1,dist2a,dist2b)

print(dist1, dist2a, dist2b)
print(ans)
fout.write (str(ans) + '\n')
fout.close()