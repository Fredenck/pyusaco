def Tuesday(one,two,b1milk):
    for i in one:
        newOne = one.copy()
        newOne.remove(i)
        newTwo = two.copy()
        newTwo.append(i)
        Wednesday(newOne,newTwo,b1milk-i)
def Wednesday(one,two,b1milk):
    for i in two:
        newOne = one.copy()
        newOne.append(i)
        newTwo = two.copy()
        newTwo.remove(i)
        Thursday(newOne,newTwo,b1milk+i)
def Thursday(one,two,b1milk):
    for i in one:
        newOne = one.copy()
        newOne.remove(i)
        newTwo = two.copy()
        newTwo.append(i)
        Friday(newOne,newTwo,b1milk-i)
def Friday(one,two,b1milk):
    for i in two:
        pos.add(b1milk+i)
fin = open ('backforth.in', 'r')
fout = open ('backforth.out', 'w')
first = list(map(int, fin.readline().strip().split(" ")))
second = list(map(int, fin.readline().strip().split(" ")))
pos = set()

Tuesday(first,second,1000)

print(len(pos))

fout.write (str(len(pos)) + '\n')
fout.close()
