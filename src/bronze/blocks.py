# def magic(alist):#takes ["fox","box"] as input
#     needed = list(alist[0])#['f','o','x']
#     orig = list(alist[0])
#     for i in alist[1]:
#         if i not in orig:
#             needed.append(i)
#             
#     needed2 = list(alist[1])
#     orig = list(alist[1])
#     for i in alist[0]:
#         if i not in orig:
#             needed2.append(i)
#     if len(needed)>len(needed2):
#         return needed
#     return needed2
def magic(alist):
    needed = []
    prev = []
    for j in alist:
        for i in j:##each word
            if i in prev:
                continue
            one = alist[0].count(i)
            two = alist[1].count(i)
            needed += [i]*max(one,two)
            prev.append(i)
    return needed
#read in
fin = open ('blocks.in', 'r')
fout = open ('blocks.out', 'w')
N = int(fin.readline().strip())
blocks = []
for i in range(N):
    front,back = map(str, fin.readline().split())
    blocks.append([front,back])

pos = 2**N
need = [0]*26


for i in range(N):#["fox","box"]
    combined = magic(blocks[i])
    for j in combined:
        letterPosition = ord(j)-96-1#'a'=>0
        need[letterPosition] += 1
    #for j in blocks[i]:#'fox'   
        #for k in j:#'f'
        #    letterPosition = ord(k)-96
        #    needed[letterPosition] += 1
print(need)
#code

for i in need:
    fout.write (str(i) + '\n')
fout.close()