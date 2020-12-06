uniquekey = list()
uniquekeylength = 0
somelengtg = 0
finalcnt = 0
string = ''
somelist= list()
newline =False
counterLine = 0
with open('test.txt') as input:
    for x in input.readlines():

        if x != '\n':
            counterLine += 1
            string = x.rstrip('\n')
            for y in string:
                if y not in uniquekey:
                    uniquekey.append(y)
                else:
                    somelist.append(y)
            line = 0
        elif x == '\n':
            if len(uniquekey) != 0 and len(somelist) == 0 and counterLine >= 2:
                finalcnt += len(somelist)
            elif len(uniquekey) != 0 and len(somelist) == 0 and counterLine ==1:
                finalcnt += len(uniquekey)
            elif len(uniquekey) != 0 and len(somelist) != 0 and counterLine >1:
                if len(somelist) == 0 :
                    finalcnt += len(somelist)
                else:
                    newlist = list()
                    for x in somelist:
                        if x not in newlist:
                            newlist.append(x)
                    finalcnt += len(newlist)
            counterLine = 0
            uniquekeylength += len(uniquekey)

            somelengtge = len(uniquekey)
            uniquekey.clear()
            somelist.clear()

print(finalcnt)