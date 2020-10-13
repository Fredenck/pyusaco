#read in
fin = open ('moosick.in', 'r')
fout = open ('moosick.out', 'w')

N = int(fin.readline().strip())
song = []
for i in range(N):
    note = int(fin.readline().strip())
    song.append(note)

C = int(fin.readline().strip())
ruminant = []
for i in range(C):
    note = int(fin.readline().strip())
    ruminant.append(note)
ruminant.sort()
    
instances = []
for i in range(0,len(song)-C+1):
    flag = False
    posRum = []
    for j in range(C):
        posRum.append(song[i+j])
        
    posRum.sort()
    dif = posRum[0]-ruminant[0]
    for k in range(1,len(posRum)):
        if (posRum[k]-ruminant[k]) == dif:
            flag = True
        else:
            flag = False
            break
    if flag:
        instances.append(i+1)
        

#https://stackoverflow.com/questions/27974126/how-to-get-all-combinations-of-length-n-in-python
# combs = list(itertools.combinations(ruminant, 2))#gets all combinations in groupings of 2 from list ruminant
# difList = []
# for i in combs:#get [1,2,3] from 7-4,7-6,6-4
#     dif = abs(i[1]-i[0])
#     difList.append(dif)
# print(difList)

# instances = []
# for i in range(0,len(song)-C+1):
#     posRum = []
#     for j in range(C):
#         posRum.append(song[i+j])
#     posCombs = list(itertools.combinations(posRum, 2))#get combinations of 2 from list posRum
#     difPosList = []
#     for k in posCombs:#get differences in the possible ruminant
#         dif = abs(k[1]-k[0])
#         difPosList.append(dif)
#     if sorted(difPosList) == sorted(difList):
#         instances.append(i+1)
    
    
print(instances)
fout.write(str(len(instances))+"\n")
for i in instances:
    fout.write(str(i) + '\n')
fout.close()