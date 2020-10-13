import itertools
#read in
fin = open ('guess.in', 'r')
fout = open ('guess.out', 'w')
N = int(fin.readline().strip())
animals = []
num = -1
maxSum = -1
for i in range(N):
    animal = list(fin.readline().split())
    if num < int(animal[1]):
        num = int(animal[1])
        mostAnimal = animal
    animals.append(animal)

#split animals into all possible sublists by 2
a=list(itertools.combinations(animals, 2))#https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways
for j in a:
    i = []
    i.append(j[0][2:])
    i.append(j[1][2:])
    #count duplicates in 2 lists
    sum = len(set(i[0]) & set(i[1]))#https://stackoverflow.com/questions/4775004/count-duplicates-between-2-lists
    print(set(i[0]) & set(i[1]))
    if sum>maxSum:
        maxSum = sum
    if maxSum == 4:
        pass
if maxSum >= num:
    maxSum = num-1

print(maxSum+1)

fout.write (str(maxSum+1) + '\n')
fout.close()