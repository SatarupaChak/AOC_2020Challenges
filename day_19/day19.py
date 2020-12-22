import re
rulesnumbers= [{0: 8}, {0: 11}]
possibletypes =list()
somestring=''
justValues= [8, 11]
with open('rulematcher.txt') as rulematchinput:
    for x in rulematchinput.readlines():
        wantednumber = x.rstrip('\n').split(':')
        if int(wantednumber[0]) == 0 :
            print(wantednumber[1])
            m = re.search('\|',wantednumber[1])
            if m == None:
              numbers = wantednumber[1].split(' ')
              for evr in numbers:
                  if evr != '':
                     rulesnumbers.append({int(wantednumber[0]):int(evr)})
                     justValues.append(int(evr))
            if m!=None:
                numbs = wantednumber[1].split('|')
                numbers_1 = numbs[0].split(' ')
                numbers_2 = numbs[1].split(' ')
                for y in numbers_1:
                    if y != '':
                     rulesnumbers.append({int(wantednumber[0]):int(y)})
                     justValues.append(int(evr))
                for j in numbers_2:
                    if j != '':
                      rulesnumbers.append({int(wantednumber[0]):int(j)})
                      justValues.append(int(evr))

        else:
            for x in justValues:
             if int(wantednumber[0]) == x:
              if wantednumber[1] == 'a':
                  somestring+='a'
                  rulesnumbers.remove(wantednumber[1])
              elif wantednumber[1] == 'b':
                  somestring += 'b'
                  rulesnumbers.remove(wantednumber[1])
              else:
                  m = re.search('\|', wantednumber[1])
                  if m !=None:
                          numbs = wantednumber[1].split('|')
                          numbers_1 = numbs[0].split(' ')
                          numbers_2 = numbs[1].split(' ')
                          for y in numbers_1:
                              if y != '':
                                  rulesnumbers.append({int(wantednumber[0]):int(y)})
                                  justValues.append(int(y))
                          for j in numbers_2:
                              if j != '':
                                  rulesnumbers.append({int(wantednumber[0]):int(j)})
                                  justValues.append(int(j))


print(rulesnumbers)
print(justValues)
