fin = open ('tttt.in', 'r')
fout = open ('tttt.out', 'w')

board = []
for i in range(3):
    board.append(fin.readline().strip())

single = 0
double = 0
won = []
flag = []
for i in range(3):
#vertical
    if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] not in won:
        single += 1
        won.append(board[0][i])
    else:
        if board[0][i] == board[1][i] or board[1][i] == board[2][i] or board[0][i] == board[2][i]:
            flag.append(board[0][i])
            flag.append(board[1][i])
            flag.append(board[2][i])
            flag = list(set(flag))
            if flag not in won and len(flag) == 2:
                won.append(flag)
                double += 1
            flag = []
    #horizontal
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] not in won:
        single += 1
        won.append(board[i][0])
    else:
        if board[i][0] == board[i][1] or board[i][1] == board[i][2] or board[i][0] == board[i][2]:
            flag.append(board[i][0])
            flag.append(board[i][1])
            flag.append(board[i][2])
            flag = list(set(flag))
            if flag not in won and len(flag) == 2:
                won.append(flag)
                double += 1
            flag = []
#TL to BR
if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] not in won:
    single += 1
    won.append(board[0][0])
else:
    if board[0][0] == board[1][1] or board[1][1] == board[2][2] or board[0][0] == board[2][2]:
        flag.append(board[0][0])
        flag.append(board[1][1])
        flag.append(board[2][2])
        flag = list(set(flag))
        if flag not in won and len(flag) == 2:
            won.append(flag)
            double += 1
        flag = []
#TR to BL
if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] not in won:
    single += 1
    won.append(board[0][2])
else:
    if board[0][2] == board[1][1] or board[1][1] == board[2][0] or board[0][2] == board[2][0]:
        flag.append(board[2][0])
        flag.append(board[1][1])
        flag.append(board[0][2])
        flag = list(set(flag))
        if flag not in won and len(flag) == 2:
            won.append(flag)
            double += 1
        flag = []

fout.write (str(single) + '\n' + str(double) + '\n')
fout.close()
