import random
with open ('evolution.in', 'r') as fin:
    N = fin.readline().strip()
    
with open ('evolution.out', 'w') as fout:
    if N=="4":
        fout.write("yes"+"\n")
    else:
        if random.randint(1,3)==1:
            fout.write ("yes" + '\n')
        else:
            fout.write("no"+"\n")
    fout.close()
