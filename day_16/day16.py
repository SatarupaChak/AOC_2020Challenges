classnumbers =list()
rownumbers =list()
seatnumbers=list()
nearby =list()
with open('day16.txt') as inputfile:
   for x in inputfile.readlines():
     if x.startswith('class:'):
       srinf = x.rstrip('\n')
       seprat = srinf.split(':')
       numberRanges = seprat[1].split('or')
       startandend =numberRanges[0].split('-')
       startrange = int(startandend[0])
       endrange = int(startandend[1])
       si= startrange
       se =endrange
       for i in range(si,se+1):
           classnumbers.append(i)
       # second set
       startandend = numberRanges[1].split('-')
       startrange = int(startandend[0])
       endrange = int(startandend[1])
       si = startrange
       se = endrange
       for i in range(si, se+1):
           classnumbers.append(i)
     elif x .startswith('row:'):
         srinf = x.rstrip('\n')
         seprat = srinf.split(':')
         numberRanges = seprat[1].split('or')
         startandend = numberRanges[0].split('-')
         startrange = int(startandend[0])
         endrange = int(startandend[1])
         si = startrange
         se = endrange
         for i in range(si, se + 1):
             rownumbers.append(i)
         # second set
         startandend = numberRanges[1].split('-')
         startrange = int(startandend[0])
         endrange = int(startandend[1])
         si = startrange
         se = endrange
         for i in range(si, se + 1):
             rownumbers.append(i)
     elif x.startswith('seat:'):
         srinf = x.rstrip('\n')
         seprat = srinf.split(':')
         numberRanges = seprat[1].split('or')
         startandend = numberRanges[0].split('-')
         startrange = int(startandend[0])
         endrange = int(startandend[1])
         si = startrange
         se = endrange
         for i in range(si, se + 1):
             seatnumbers.append(i)
         # second set
         startandend = numberRanges[1].split('-')
         startrange = int(startandend[0])
         endrange = int(startandend[1])
         si = startrange
         se = endrange
         for i in range(si, se + 1):
             seatnumbers.append(i)


print(classnumbers)
anotherlist= list()
with open('nearby.txt') as inputfilenearby:
    for x in inputfilenearby.readlines():
        if x.startswith('nearby tickets'):
            print('do nothing')
        else:
          values = x.rstrip('\n').split(',')

          if int(values[0]) not in classnumbers:
                  anotherlist.append('firstcol not in class')
                  if int(values[0]) not in rownumbers:
                      anotherlist.append('firstcol not in rownumbers')
                  if int(values[0]) not in seatnumbers:
                      anotherlist.append('firstcol not in seatnumbers')
                  if int(values[1]) not in classnumbers:
                     anotherlist.append('secondcol not in class')
                  if int(values[1]) not in rownumbers:
                        anotherlist.append('secondcol not in rownumbers')
                  if int(values[1]) not in seatnumbers:
                         anotherlist.append('secondcol not in seatnumbers')
                  if int(values[2]) not in classnumbers:
                       anotherlist.append('third not in class')
                  if int(values[2]) not in rownumbers:
                        anotherlist.append('third not in rownumbers')
                  if int(values[2]) not in seatnumbers:
                       anotherlist.append('third not in seatnumbers')
          elif int(values[0]) in classnumbers:
              print('ok')



print(anotherlist)




# for value in nearby:
#     if value not in numbers:
#         nearby.remove(value)
#
# scan_error_rate =0
# for z in c:
#     scan_error_rate+=z

#print(scan_error_rate)


