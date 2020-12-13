newarr = list()
starttime= 0
with open('newinput.txt') as inputfile:
    arr = inputfile.readlines()
    for x in range(0,len(arr)-1):
        starttime= int(arr[x].rstrip('\n'))
        print(starttime)
    for y in range(1,len(arr)):
      newvalues =arr[y].split(',')
      for z in newvalues:
          if z != 'x':
              newarr.append(int(z.rstrip('\n')))


print(newarr)
minwait = starttime
bus=0

for elem in newarr:
    waittime= elem - (starttime % elem)
    if waittime < minwait:
        bus= elem
        minwait = waittime

print(minwait *bus)