#read in
fin = open ('guess.in', 'r')
fout = open ('guess.out', 'w')
N = int(fin.readline().strip())
characteristics = []
animals = []
num = -1
for i in range(N):
    animal = list(fin.readline().split())
    for j in range(int(animal[1])):
        characteristics.append(animal[j+2])
    if num < int(animal[1]):
        num = int(animal[1])
        mostAnimal = animal
    animals.append(animal)

danimals = []
danimal = animals.copy()
for i in range(len(animals)):
    if int(animals[i][1]) == num:
        del danimal[i]
        danimals.append(danimal)
        danimal = animals.copy()
        
maxSim = -1
for k in danimals:
    for j in k:
        similar = 0
        for i in mostAnimal[2:]:
            if i in j:
                similar += 1
        if similar>maxSim:
            maxSim = similar

print(maxSim+1)

fout.write (str(maxSim+1) + '\n')
fout.close()