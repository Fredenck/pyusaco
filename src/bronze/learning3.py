def compare2(a,b,code):
    if code == "SS":
        return int(b-a)
    elif code == "NSNS":
        return 0
    elif (code == "NSS") or (code == "SNS"):
        return int((b-a)/2)
#         if ((b-a)/2).is_integer():
#             return (b-a)/2+1
#         else:
#             return int((b-a)/2)+1
#read in
fin = open ("learning.in", "r")
fout = open ("learning.out", "w")
N,A,B = map(int,fin.readline().strip().split())
spots,weights,total = [],[],[]
for i in range(N):
    posSpot, W = fin.readline().split()
    total.append([int(W),posSpot])
total.sort()
print(total)

metA,metB,AinBetween = False, False, False

d = 0
for i in range(N-1):
    if not metA:#look for A and it's corner cases
        if (total[i][0]>A) and (total[i][1]=="S"):#if A is before the first cow
            metA = True
            d += (total[i][0]-A)
        elif total[i][0] == A:#cur cow is A
            metA = True
        elif (total[i][0]<A<total[i+1][0]):#A is between 2 cows
            metA = True
            MP = (total[i][0]+total[i+1][0])/2
            # and ((total[i][1]=="S") or (total[i+1][1]=="S"))
            #the MP will be counted
            
            #SEE LATETRR
            if (A<MP) and (total[i][1]=="S"):#if A=MP, only do one of these
                d += MP-total[i][0]+1
            elif (A>=MP) and (total[i+1][1]=="S"):
                d += total[i+1][0]-MP+1
            if MP.is_integer():#count the MP
                d += 1
            d = int(d)
            AinBetween = True
    if metA:
        if metB:
            break
        if AinBetween:#when I did the corner case with A between 2 cows, I already counted an extra
            AinBetween = False
            continue
        if (total[-1]==total[i+1]) and (total[i+1][0]<B) and (total[i+1][1]=="S"):#if B is after the last one
            metB = True
            d += compare2(total[i][0], total[i+1][0], total[i][1]+total[i+1][1]) + (B-total[i+1][0])
        elif total[i+1][0] == B:#if B is the last cow
            metB = True
            d += compare2(total[i][0], total[i+1][0], total[i][1]+total[i+1][1])
        elif total[i][0]<B<total[i+1][0]:#in between
            MP = (total[i][0]+total[i+1][0])/2
            if (B<MP) and (total[i][1]=="S"):
                d += MP-total[i][0]+1
            elif (B>=MP) and (total[i+1][1]=="S"):
                d += total[i+1][0]-MP+1
            if MP.is_integer():#count the MP
                d += 1
            d = int(d)
        else:
            d += compare2(total[i][0], total[i+1][0], total[i][1]+total[i+1][1])
        print(d)

print(d)
fout.write (str(int(d)) + "\n")
fout.close()