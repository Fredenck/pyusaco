def Tf():
    log2 = log.copy()
    prev = log2[0]
    for i in range(1, len(log2)):
        if log2[i] == prev and (prev != 0 and prev != -1):
            return True
        prev = log2[i]
    return False
def main():#read in
    ans = -1
    if (log[0] == 0 or log[0] == -1):
        log[0] = 0
#         print(log)
        for i in range(N-1,-1,-1):#back to front
            if log[i] >= 1 and log[i-1] == -1:
                log[i-1] = log[i]-1
#         print(log)
        if Tf():
            return ans, "false"
        ans = log.count(0)
        ansMax = ans
        for i in log:
            if i == -1:
                ansMax += 1
        return ans, ansMax
    else:
        return ans, 'false'

fin = open ('taming.in', 'r')
fout = open ('taming.out', 'w')
N = int(fin.readline().strip())
log = list(map(int, fin.readline().split()))

ans, ansMax = main()


print(ans, ansMax)
if ansMax == 'false':
    fout.write('-1\n')
else:
    fout.write (str(ans) + ' ' + str(ansMax)+'\n')
fout.close()