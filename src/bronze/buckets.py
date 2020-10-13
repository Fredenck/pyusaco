fin = open ('buckets.in', 'r')
fout = open ('buckets.out', 'w')

for i in range(10):
    row = list(fin.readline().strip())
    if "L" in row:
        lake = (i,row.index("L"))
    if "B" in row:
        barn = (i,row.index("B"))
    if "R" in row:
        rock = (i,row.index("R"))

print(lake, barn, rock)
ans = (abs(lake[0]-barn[0]))+(abs(lake[1]-barn[1]))-1
if (((barn[0]<=rock[0]<=lake[0]) or (lake[0]<=rock[0]<=barn[0])) and (barn[1]==lake[1]==rock[1])) or (((barn[1]<=rock[1]<=lake[1]) or (lake[1]<=rock[1]<=barn[1])) and (barn[0]==lake[0]==rock[0])):#vertical, rock in between barn and lake
    ans+=2
print(ans)
fout.write (str(ans) + '\n')
fout.close()