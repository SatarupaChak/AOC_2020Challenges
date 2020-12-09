
another= list ()
with open('sometext.txt') as inputfile:
    somel = list()

    m = inputfile.readlines()
    for x in range(25,len(m)):
        print(int(m[622]))
        number = int(m[x].rstrip('\n'))
        start = x-25
        end = start+25
        newl = m[start:end]
        for y in range(len(newl)):
            anotherNum = int(newl[y].rstrip('\n'))
            for z in range(y+1,len(newl)):
                thirdnum = int(newl[z].rstrip('\n'))
                if thirdnum + anotherNum == number:
                    if x not in somel:
                        somel.append(x)



