num = 373803594
numb = 127
#https://stackoverflow.com/questions/18305843/find-all-subsets-that-sum-to-a-particular-value
fatherlist = list()
with open ("sometext.txt") as inputfile:
     m = inputfile.readlines()
     for x in range(len(m)):
         fatherlist.append(int(m[x].rstrip('\n')))



print(fatherlist)