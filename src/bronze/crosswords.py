#read in
fin = open ('crosswords.in', 'r')
fout = open ('crosswords.out', 'w')
N,M = map(int, fin.readline().split())

crossword = []
for i in range(N):
    crossword.append(list(fin.readline().strip()))

clues = set()#if it is both vertical and horizontal, then it is only counted once
for i in range(N):#horizontal
    for j in range(M-2):
        if (crossword[i][j] == crossword[i][j+1] == crossword[i][j+2] == "."):
            if j == 0:
                clues.add((i+1,j+1))
            else:
                if crossword[i][j-1]=="#":
                    clues.add((i+1,j+1))
for i in range(N-2):#vertical
    for j in range(M):
        if crossword[i][j] == crossword[i+1][j] == crossword[i+2][j] == ".":
            if i == 0:
                clues.add((i+1,j+1))
            else:
                if crossword[i-1][j]=="#":
                    clues.add((i+1,j+1))

print(clues)
clues = sorted(list(clues))
fout.write (str(len(clues)) + '\n')
for i in clues:
    fout.write (str(i[0]) + " " + str(i[1]) + '\n')
fout.close()