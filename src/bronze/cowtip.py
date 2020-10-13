def toggle(map,x,y):
    for i in range(x):
        for j in range(y):
            if map[i][j] == '1':
                map[i][j] = '0'
            else:
                map[i][j] = '1'
    return map
#read in
fin = open ('cowtip.in', 'r')
fout = open ('cowtip.out', 'w')
N = int(fin.readline().strip())
map = []
for i in range(N):#read in map of cows reversed so i can start from top left cow and check if it's a tipped or not
    row = list(fin.readline().split()[0])
    map.append(row)


count = 0
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if map[i][j] == '1':
            count += 1
            map = toggle(map,i+1,j+1)
            

# totalList.append()


print(count)
fout.write (str(count) + '\n')
fout.close()