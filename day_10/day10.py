someList = list()
difflist =list()
difflist_2 = list()
with open('smallInput.txt') as inputFile:
    alllines = inputFile.readlines()
    for x in alllines:
        someList.append(int(x.rstrip('\n')))

print(sorted(someList))
p =0
while p < len(sorted(someList))-1:
    val = sorted(someList)[p]
    val2= sorted(someList)[p+1]
    if val2 -val == 3:
        print("difference of 3")
        difflist.append("difference of 3")



    elif val2-val == 1:
        print("difference of one")
        difflist_2.append("difference of 1")
    p=p+1




print((len(difflist)+1) * (len(difflist_2)+1))
print(len(difflist_2))

print(len(someList))