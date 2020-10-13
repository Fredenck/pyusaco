def areaOfRectangle(x1,y1,x2,y2):
    return abs(x2-x1)*abs(y2-y1)

def main(x1,y1,x2,y2,x3,y3,x4,y4):
    s1 = abs(max(x1,x2,x3,x4))-abs(min(x1,x2,x3,x4))
    s2 = abs(max(y1,y2,y3,y4))-abs(min(y1,y2,y3,y4))
    side = max(s1,s2)
    return side*side
#read in
fin = open ('square.in', 'r')
fout = open ('square.out', 'w')
x1,y1,x2,y2 = map(int, fin.readline().split())
x3,y3,x4,y4 = map(int, fin.readline().split())

ans = main(x1,y1,x2,y2,x3,y3,x4,y4)

print(ans)
fout.write (str(ans) + '\n')
fout.close()