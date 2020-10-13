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
i = 1
# prev = [0,0,0]
newArray = [7,7,7]
for j in range(len(diary)):
    while array[i] == [0,0,0]:
        i += 1
        if i >= len(array):
            break
    if i >= len(array):
        break
    newArray = [sum(x) for x in zip(newArray, array[i])]
#     newArray = [sum(x) for x in zip(array[0], array[i])]
    idx = indices = [i for i, x in enumerate(newArray) if x == max(newArray)]
    if max(newArray) >= curMax and cowUp != idx:
        cowUp = idx
        curMax = max(newArray)
        count += 1
        amountUp = newArray.count(curMax)
    else:
#         curMax = max(newArray)
        idx = indices = [i for i, x in enumerate(newArray) if x == max(newArray)]
        if cowUp != idx:
            cowUp = idx
            count += 1
        amountUp = newArray.count(curMax)
    if amountUp != newArray.count(curMax) and max(newArray) == curMax:
        idx = indices = [i for i, x in enumerate(newArray) if x == max(newArray)]
        cowUp = idx
        count += 1
        amountUp = newArray.count(curMax)
#     prev = array[i]
    i += 1
#     if i >= len(array):
#         break
# print(count)
# print(newArray)
fout.write (str(count) + '\n')
fout.close()