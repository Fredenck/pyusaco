def common(pos2,pos3):#converts pos2 and pos3 to B10, and finds the one common value
    b10 = []
    for i in pos2:
        #https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int
        b10.append(int(i, 2))#add base2 to set
    for i in pos3:
        converted = int(i, 3)
        print(i,converted)
        if converted in b10:
            return converted
#     print(b10)
#read in
fin = open ('digits.in', 'r')
fout = open ('digits.out', 'w')
B2 = fin.readline().strip()
B3 = fin.readline().strip()

pos2,pos3 = [],[]
for i in range(len(B2)):#each iteration is one place value
    alter = list(B2)#1010->['1','0','1','0']
    alter[i] = str(abs(int(alter[i])-1))#1->0;0->-1->1(changes num)
    alter = ''.join(alter)
    pos2.append(alter)#['0010','1110','1000','1011']

for i in range(len(B3)):#each iteration is one place value
    for j in range(1,3):#twice, because there are 3 nums in b3, and you want to change to the other 2
        alter = list(B3)
        if alter[i] == "0":
            alter[i] = str(abs(int(alter[i])+j))#0->1;0->2
        elif alter[i] == "1":
            if j==1:
                alter[i] = "0"
            else:
                alter[i] = "2"
        elif alter[i] == "2":
            alter[i] = str(abs(int(alter[i])-j))#2->1;2->0
        alter = ''.join(alter)
        pos3.append(alter)#['112', '012', '202', '212', '211', '210']

num = common(pos2,pos3)
    
print(num)


fout.write (str(num) + '\n')
fout.close()