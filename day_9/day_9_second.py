num = 373803594
numb = 127
fatherlist = list()
with open ("sometext.txt") as inputfile:
     m = inputfile.readlines()
     for x in range(len(m)):
         fatherlist.append(int(m[x].rstrip('\n')))



print(fatherlist)