finallist = {}
with open('somefile.txt') as inputfile:
    arr = inputfile.readlines()
    for x in arr:
        if x.startswith('mask'):
            val = x.rstrip('\n')
            maskedval =val.split(' = ')
        elif x.startswith('mem'):
            val2 = x.rstrip('\n')
            newval =val2.split(' = ')
            integer =int(newval[1].lstrip(' '))
            dectobin = "{0:36b}".format(integer)

            sring = ''
            print(len(maskedval[1]))
            print(len(dectobin))
            for maskedchar  in range(len(maskedval[1])):
                for  integerchar in  range(len(dectobin)):
                  if maskedchar == integerchar:
                    if maskedval[1][maskedchar] == 'X':
                        sring += 'X'
                    elif maskedval[1][maskedchar] == '1':
                         sring += '1'
                    elif maskedval[1][maskedchar] == '0':
                        if dectobin[integerchar] == ' ':
                            sring += '0'
                        else:
                            sring+= dectobin[integerchar]





            print(len(sring))
            finallist[newval[0]] = sring


print(finallist)