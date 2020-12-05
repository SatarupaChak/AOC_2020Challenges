import re

newList = list()
tempdict= dict()
mentionedkeys = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]


def readMe():
    with open('text.txt', 'r') as infile:
        jewelsString = []
        for line in infile:
            if line != '\n':
                if any(ext in line for ext in mentionedkeys):
                    print(line)
                    newstreng = line.rstrip('\n')
                    jewelsString.append(newstreng)
                    print('jewelstring')
                    print(jewelsString)



            elif line == '\n':
                 print('empty space')
                 print('here is hewwel string')
                 print(jewelsString)
                 if len(jewelsString) ==1:
                     getList(newstreng)
                     jewelsString.clear()
                 elif len(jewelsString) >1:
                       newmagicstr =''
                       for x in jewelsString:
                          newmagicstr +=' ' + x
                       getList(newmagicstr)
                       jewelsString.clear()






def newToSingle(line, strng):
  strng += line
  return strng;


boolList =list()
finalList =list()
def getList(line):
    print(line)
    if (line.find("byr") != -1) and (line.find("iyr")) != -1 and (line.find("eyr") != -1) and (line.find("hgt") != -1) and (line.find("hcl") != -1) and  (line.find("ecl") != -1) and (line.find("pid") != -1) :
        newList.append(line)




def secondPart(line):
        newline = line.split(" ")
        for nl in newline:
            if nl.startswith('byr'):
                inde = nl.split(':')
                print(inde)
                if int(inde[1]) >= 1920 and int(inde[1]) <=2002:
                    boolList.append(True)
                else:
                    boolList.append(False)
            elif nl.startswith('hgt'):
                inde = nl.split(':')
                if inde[1].endswith("cm"):
                    val1 = inde[1].rstrip("cm")
                    if int(val1) >= 150 or int(val1)<=190:
                        boolList.append(True)
                    else:
                        boolList.append(False)
                elif inde[1].endswith("in"):
                    val2 = inde[1].rstrip("in")
                    print()
                    if int(val2) >= 59 or int(val2) <= 76:
                        boolList.append(True)
                    else:
                        boolList.append(False)
                else:
                     boolList.append(False)

            elif nl.startswith('iyr'):
                inde = nl.split(':')
                if int(inde[1]) >= 2010 and int(inde[1]) <= 2020:
                    boolList.append(True)
                else:
                    boolList.append(False)
            elif nl.startswith('eyr'):
                inde = nl.split(':')
                if int(inde[1]) >= 2020 and int(inde[1]) <= 2030:
                    boolList.append(True)
                else:
                    boolList.append(False)
            elif nl.startswith('hcl'):
                inde = nl.split(':')
                pattern = '^#[a-f0-9]{6}'
                res =re.match(pattern,inde[1])
                if res is not None :
                  boolList.append(True)
                else:
                  boolList.append(False)
            elif nl.startswith('ecl'):
                inde = nl.split(':')
                if (inde[1].find('amb') != -1) or (inde[1].find('blu') != -1)  or (inde[1].find('brn') != -1)  or (inde[1].find('gry')!= -1)  or (inde[1].find('grn') != -1)  or (inde[1].find('hzl')!= -1)  or (inde[1].find('oth')!= -1) :
                    boolList.append(True)
                else: boolList.append(False)
            elif nl.startswith('pid'):
                 newinde = nl.split(':')
                 pattern = '[0-9]'
                 lengStr = len(newinde[1])
                 res2 = re.match(pattern, newinde[1])
                 if res2 is not None and lengStr == 9 :
                      boolList.append(True)
                 else:
                        boolList.append(False)







       # newList.append(line)



# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


readMe()


print(newList)
