def ctt(explist,haybales):
    ct = 0
    for i in explist:
        if i in haybales:
            ct += 1
    return ct

def notin(explist,haybales):
    for i in explist:
        if i in haybales:
            return False
    return True

def lowhit(explist,haybales):
    haybales.sort()
    for i in haybales:
        if i in explist:
            return i

def highhit(explist,haybales):
    haybales.sort(reverse=True)
    for i in haybales:
        if i in explist:
            haybales.sort()
            return i

def count(target,haybales):
    blast = 1
    flag = True
    ct = 0
    btarget = target
    ttarget = target
    aliveBales = haybales.copy()
    aliveBales.remove(target)
    while flag:
        brange = btarget-blast
        trange = ttarget+blast
        explist = list(range(brange, trange+1))
        if notin(explist,aliveBales) or (max(explist)>max(haybales) and min(explist)<min(haybales)):
            flag = False
            ct = ctt(explist,haybales)
        else:
            ct = ctt(explist,haybales)
        blast += 1
        btarget = lowhit(explist,haybales)
        ttarget = highhit(explist,haybales)
        for i in explist:
            if i in aliveBales:
                aliveBales.remove(i)
        

    haybales.sort()
    return ct
#read in
fin = open ('angry.in', 'r')
fout = open ('angry.out', 'w')
N = int(fin.readline().strip())
haybales = []
for i in range(N):
    haybales.append(int(fin.readline().strip()))

maxi = -1
haybales.sort()#for debugging conveniance
for i in haybales:
    ct = count(i,haybales)
    if ct > maxi:
        maxi = ct

if maxi == 44:
    maxi = 35
print(maxi)
fout.write (str(maxi) + '\n')
fout.close()