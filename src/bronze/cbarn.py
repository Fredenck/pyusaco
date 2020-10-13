#read in
fin = open ('cbarn.in', 'r')
fout = open ('cbarn.out', 'w')
N = int(fin.readline().strip())
doors = []
for i in range(N):
    doors.append(int(fin.readline().strip()))
sum = sum(doors)
min = 1000000000
for i in range(N):
    left = 0
    subtr = sum
    for j in range(N-1):
        subtr -= doors[(i+j)%N]
        left += subtr
    print(left)
    if left < min:
        min = left
print(min)
fout.write (str(min) + '\n')
fout.close()