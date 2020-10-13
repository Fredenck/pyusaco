#read in input
fin = open ('mixmilk.in', 'r')
fout = open ('mixmilk.out', 'w')
capacity = []
amount = []
for i in range(3):
    cap, amnt = map(int, fin.readline().split())
    capacity.append(cap)
    amount.append(amnt)

for i in range(1,101):
    i = i % 3
    if amount[i]+amount[i-1] <= capacity[i]:#if you can put ALL of the milk into the next container
        amount[i] += amount[i-1]
        amount[i-1] = 0
    elif amount[i] == capacity[i]:#all are full
        continue
    elif 1==2:
        continue
    else:#you have leftovers on the giving end, and the recieving is full
        need = capacity[i]-amount[i]
        amount[i] += need
        amount[i-1] -= need
        

# print(amount)
# print(capacity)
for i in range(3):
    fout.write (str(amount[i]) + '\n')
    
fout.close()
