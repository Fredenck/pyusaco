#read in
fin = open ('hps.in', 'r')
fout = open ('hps.out', 'w')
N = int(fin.readline().strip())
log = []
case1 = 0
case2 = 0
for i in range(N):
    first,second = map(int, fin.readline().split())
    if first != second:#otherwise they tie, which leads to no matter what "not a win"
        if (first == 1 and second == 2) or (first == 3 and second == 1) or (first == 2 and second == 3):
            case1 += 1
        if (first == 1 and second == 3) or (first == 3 and second == 2) or (first == 2 and second == 1):
            case2 += 1
        
print(max(case1,case2))
fout.write (str(max(case1,case2)) + '\n')
fout.close()