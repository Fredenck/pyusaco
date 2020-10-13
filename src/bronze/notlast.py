#read in
fin = open ('notlast.in', 'r')
fout = open ('notlast.out', 'w')
N = int(fin.readline().strip())

key = [0]*7
for i in range(N):
    cowName, amount = fin.readline().split()
    if cowName == "Bessie":
        key[0] += int(amount)
        continue
    if cowName == "Elsie":
        key[1] += int(amount)
        continue
    if cowName == "Daisy":
        key[2] += int(amount)
        continue
    if cowName == "Gertie":
        key[3] += int(amount)
        continue
    if cowName == "Annabelle":
        key[4] += int(amount)
        continue
    if cowName == "Maggie":
        key[5] += int(amount)
        continue
    if cowName == "Henrietta":
        key[6] += int(amount)
        continue
    
smallest = min(key)

if len(set(key)) == 1:
    ans = "Tie"
else:
    #https://stackoverflow.com/questions/2186656/how-can-i-remove-all-instances-of-an-element-from-a-list-in-python
    key2 = [x for x in key if x != smallest]#remove all instances of smallest from key
    secondSmallest = min(key2)

    count = 0
    cows = ["Bessie","Elsie","Daisy","Gertie","Annabelle","Maggie","Henrietta"]
    for i in range(len(key)):
        if key[i] == secondSmallest:
            count += 1
            if count >= 2:
                ans = "Tie"
                break
            else:
                ans = cows[i]
            

print(ans)
fout.write (ans + '\n')
fout.close()