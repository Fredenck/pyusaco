#read in
fin = open ('guess.in', 'r')
fout = open ('guess.out', 'w')
N = int(fin.readline().strip())
characteristics = []
animals = []
curAnimals = []
num = -1
for i in range(N):
    animal = list(fin.readline().split())
    for j in range(int(animal[1])):
        characteristics.append(animal[j+2])
    if num<int(animal[1]):
        num = int(animal[1])
        largestAnimal = animal[0]
    animals.append(animal)
    
count = 0
used = []
j = 0
ct = 0
curAnimal = animals[ct][0]
for i in list(set(characteristics)):
    if characteristics.count(i) > 1:#multiple animals share the same characteristic
        count += 1
#         used.append(i)
    
if num>count:
    count += 1
print(animals)
print(characteristics)
print(count)
print(num)

fout.write (str(count) + '\n')
fout.close()