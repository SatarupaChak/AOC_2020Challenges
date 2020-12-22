import re

somedict = {}
somearr = list()
with open('sometext.txt') as inputtextFile:
    for x in inputtextFile.readlines():
        i = x.find('contains')
        s = x.rstrip('\n').rstrip(')')[i + 8:]
        t= x[:i].rstrip('(').rstrip(' ')
        contentsall = t.split(' ')
        k = s.find(',')
        if k != -1:
            values = s.split(',')
            for val in values:
                somedict = {"nameofintegradeiate": val, "contents": contentsall}
                if len(somearr)>0:
                  for some in somearr:
                    if [some['nameofintegradeiate']] == somedict['nameofintegradeiate']:
                        somearr.remove(some['nameofintegradeiate'].strip(''))
                        print('here')
                    elif [some['nameofintegradeiate']] != somedict['nameofintegradeiate']:
                        somearr.append(somedict)
                else:
                    somearr.append(somedict)
        else:
            somedict = {"nameofintegradeiate": s, "contents":contentsall}
            if len(somearr) > 0:
              for some in somearr:
                print(some['nameofintegradeiate'].strip(''), somedict['nameofintegradeiate'].strip(''))
                if [some['nameofintegradeiate'].strip('')] == somedict['nameofintegradeiate'].strip(''):
                    somearr.remove(some['nameofintegradeiate'].strip(''))
                    print('ok')
                    print('ok')
                elif [some['nameofintegradeiate']] != somedict['nameofintegradeiate']:
                    somearr.append(somedict)
            else:
                somearr.append(somedict)


print(somearr)


