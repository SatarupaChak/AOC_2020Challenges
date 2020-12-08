finallist = list()
parentbags =list()

def start():
    with open('newtest.txt') as infile:
        for x in infile.readlines():
            val = x.split('contain')
            newdictionary = {'ownerbag': val[0], 'childbag': val[1].rstrip('')}
            finallist.append(newdictionary)

    checker(finallist)





def checker(finallist):
    for x in finallist:
        if x['childbag'].find('shiny gold') != -1:
            y = x['ownerbag']
            parentbags.append(y)
    secondChecker(parentbags,finallist)


def secondChecker(parentbags,finallist):
    for x in finallist:
       for fin in parentbags:
          if x['childbag'].find(str(fin).split(' ')[0] + ' ' + str(fin).split(' ')[1]) != -1:
              if x['ownerbag'] not in parentbags:
                  parentbags.append(x['ownerbag'])

    thirdChecker(parentbags,finallist)

def thirdChecker(parentbags,finallist):
    for x in finallist:
        for fin in parentbags:
            if x['childbag'].find(str(fin).split(' ')[0] + ' ' + str(fin).split(' ')[1]) != -1:
                if x['ownerbag'] not in parentbags:
                    parentbags.append(x['ownerbag'])
    thirdChecker(parentbags, finallist)

    print(parentbags)

def fourthChecker(parentbags,finallist):
    for x in finallist:
        for fin in parentbags:
            if x['childbag'].find(str(fin).split(' ')[0] + ' ' + str(fin).split(' ')[1]) != -1:
                if x['ownerbag'] not in parentbags:
                    parentbags.append(x['ownerbag'])

    print(parentbags)


def fifthChecker(parentbags,finallist):
    for x in finallist:
        for fin in parentbags:
            if x['childbag'].find(str(fin).split(' ')[0] + ' ' + str(fin).split(' ')[1]) != -1:
                if x['ownerbag'] not in parentbags:
                    parentbags.append(x['ownerbag'])

    print(parentbags)

def sixthChecker(parentbags,finallist):
    for x in finallist:
        for fin in parentbags:
            if x['childbag'].find(str(fin).split(' ')[0] + ' ' + str(fin).split(' ')[1]) != -1:
                if x['ownerbag'] not in parentbags:
                    parentbags.append(x['ownerbag'])

    print(parentbags)
start()