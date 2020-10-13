fin = open ('measurement.in', 'r')
fout = open ('measurement.out', 'w')
N = int(fin.readline().strip())
array = [[0 for x in range(3)] for y in range(101)]
diary = []
count = 0
amountUp = 3
cowUp = [0,1,2]
# prev = 0#index of last checked

for i in range(3):
    array[0][i] = 7
for i in range(N):
    alist = fin.readline().strip().split(" ")
    diary.append(alist)

for i in range(len(diary)):
    day = int(diary[i][0])
    if diary[i][1] == "Mildred":
        cowNum = 0
    if diary[i][1] == "Elsie":
        cowNum = 1
    if diary[i][1] == "Bessie":
        cowNum = 2
    amount = int(diary[i][2])
    array[day][cowNum] = amount

curMax = 7
preidx = [0,1,2]
# prev = [0,0,0]
newArray = [7,7,7]
previdx = 0
for j in range(len(diary)):
    for i in range(len(array)):
        if array[i] != [0,0,0]:#next day
            newArray = [sum(x) for x in zip(newArray, array[i])]
        #     newArray = [sum(x) for x in zip(array[0], array[i])]
            idx = [i for i, x in enumerate(newArray) if x == max(newArray)]
            if idx != previdx:
                count += 1
            previdx = idx

# print(count)
fout.write (str(count) + '\n')
fout.close()