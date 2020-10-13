2011 Dec #2
http://www.usaco.org/index.php?page=viewproblem2&cpid=95
I plan to keep track of if there are at least 3 instances of a number, A, before a number, B, then A will be before B in the original. But, I don't know how to keep track of which are in front of which
#read in
fin = open ('photo.in', 'r')
fout = open ('photo.out', 'w')
N = int(fin.readline().strip())
photos = []
photo = []
for i in range(5):
    for j in range(N):
        photo.append(int(fin.readline().strip()))
    photos.append(photo)
    photo = []#list of lists with each sublist a photo
print(photos)

for i in range(5):
    for j in range(N-1):
        if photos[i][j]<photos[i][j+1]:# if cur is smaller than next
        
    
            

fout.write (str() + '\n')
fout.close()