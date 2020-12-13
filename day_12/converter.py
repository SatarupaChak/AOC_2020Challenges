directionlist =list()
with open('original.txt') as inputfile:
  for x in inputfile.readlines():
      directionlist.append(x.rstrip('\n'))


print(directionlist)