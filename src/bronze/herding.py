#read in
fin = open ('herding.in', 'r')
fout = open ('herding.out', 'w')
B,E,M = map(int, fin.readline().split())

cowList = sorted([B,E,M])
min = min(cowList[1]-cowList[0],cowList[2]-cowList[1])-1
max = max(cowList[1]-cowList[0],cowList[2]-cowList[1])-1

if min>2:
    min = 2
if (cowList[1]-cowList[0]==2) or (cowList[2]-cowList[1]==2):
    min = 1
# if (min == 0) and ((cowList[1]-cowList[0])!=(cowList[2]-cowList[1])!=(1)):
#     min = 2

if min==0:
    min=2
if ((cowList[0]+1)==cowList[1]) and ((cowList[1]+1)==cowList[2]):
    min = 0
print(min,max)
fout.write (str(min) + '\n')
fout.write (str(max) + '\n')
fout.close()