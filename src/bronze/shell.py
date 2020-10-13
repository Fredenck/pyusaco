def swapping(a,b,prev):
    a -= 1
    b -= 1
    mid = prev[a]
    prev[a] = prev[b]
    prev[b] = mid
    return prev

fin = open ('shell.in', 'r')
fout = open ('shell.out', 'w')
N = int(fin.readline().strip())
swaps, guess = [],[]
for i in range(N):
    a,b,g = map(int, fin.readline().split())
    swaps.append([a,b])
    guess.append(g)
    
prev = [1,2,3]
# switches = []
count = [0,0,0]
for i in range(N):
    prev = swapping(swaps[i][0],swaps[i][1],prev)
    gst = prev[guess[i]-1]
    count[gst-1] += 1
    
print(count)
fout.write (str(max(count)) + '\n')
fout.close()