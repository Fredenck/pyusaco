def computeTime():
    if D<st:
        return -1
    elif D==st:
        if H<st:
            return -1
        elif H==st:
            if M<st:
                return -1
            if M==st:
                return 0#all equal
    return (D-st)*1440 + (H-st)*60 + (M-st)#days,hours, mind
    #code
#read in
fin = open ('ctiming.in', 'r')
fout = open ('ctiming.out', 'w')
D, H, M = map(int, fin.readline().split())
st = 11
time = computeTime()

                

print(time)
fout.write (str(time) + '\n')
fout.close()