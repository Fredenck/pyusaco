#read in
fin = open ('cowsignal.in', 'r')
fout = open ('cowsignal.out', 'w')
M,N,K = map(int, fin.readline().split())

signal = []
for i in range(M):
    line = list(fin.readline().strip())
    signal.append(line)

newSignal = []
for i in signal:#["X", "X", "X", "."]
    for j in i:#"X"
        newSignal.append(j*K)

count = 0
new_list = [newSignal[i:i+(N)] for i in range(0, len(newSignal), N)]

for i in new_list:
    for q in range(K):
        i = ''.join(i)
        fout.write (i+"\n")
fout.close()