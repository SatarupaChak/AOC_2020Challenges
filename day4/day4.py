boolList = list()
import  re

newarr = list()
def secondPart():
    for x in range(len(newarr)):
        newline = newarr[x].split(' ')
        for nl in newline:
            if nl.startswith('byr'):
                inde = nl.split(':')
                if int(inde[1]) >= 1920 and int(inde[1]) <=2002:
                    boolList.append({True,x})
                    print(True,x)
                else:
                    boolList.append({False,x})
                    print(False, x)
            elif nl.startswith('hgt'):
                inde = nl.split(':')
                if inde[1].endswith("cm"):
                    val1 = inde[1].rstrip("cm")
                    if int(val1) >= 150 or int(val1)<=190:
                        boolList.append({True,x})
                        print(True, x)
                    else:
                        boolList.append({False,x})
                        print(False, x)
                elif inde[1].endswith("in"):
                    val2 = inde[1].rstrip("in")
                    print()
                    if int(val2) >= 59 or int(val2) <= 76:
                        boolList.append({True,x})
                        print(True, x)
                    else:
                        boolList.append({False,x})
                        print(False, x)
                else:
                     boolList.append({False,x})
                     print(False, x)

            elif nl.startswith('iyr'):
                inde = nl.split(':')
                if int(inde[1]) >= 2010 and int(inde[1]) <= 2020:
                    boolList.append({True,x})
                    print(True, x)
                else:
                    boolList.append({False,x})
                    print(False, x)
            elif nl.startswith('eyr'):
                inde = nl.split(':')
                if int(inde[1]) >= 2020 and int(inde[1]) <= 2030:
                    boolList.append({True,x})
                    print(True, x)
                else:
                    boolList.append({False,x})
                    print(False, x)
            elif nl.startswith('hcl'):
                inde = nl.split(':')
                pattern = '^#[a-f0-9]{6}'
                res =re.match(pattern,inde[1])
                if res is not None :
                  boolList.append({True,x})
                  print(True, x)
                else:
                  boolList.append({False,x})
                  print(False, x)
            elif nl.startswith('ecl'):
                inde = nl.split(':')
                if (inde[1].find('amb') != -1) or (inde[1].find('blu') != -1)  or (inde[1].find('brn') != -1)  or (inde[1].find('gry')!= -1)  or (inde[1].find('grn') != -1)  or (inde[1].find('hzl')!= -1)  or (inde[1].find('oth')!= -1) :
                    boolList.append({True,x})
                    print(True, x)
                else:
                    boolList.append({False,x})
                    print(False, x)
            elif nl.startswith('pid'):
                 newinde = nl.split(':')
                 pattern = '[0-9]'
                 lengStr = len(newinde[1])
                 res2 = re.match(pattern, newinde[1])
                 if res2 is not None and lengStr == 9 :
                      boolList.append({True,x})
                      print(True, x)
                 else:
                        boolList.append({False,x})
                        print(False, x)

secondPart()