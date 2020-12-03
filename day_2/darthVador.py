import pandas, numpy

data = pandas.read_csv('testinput.csv', sep=':')


def func0():

    for i, row in data.iterrows():
        newlist = row['rule'].split(' ')
        interval = newlist[0].split('-')
        print(newlist[1],interval)
        value = (row['value']).lstrip()
        newfunc(value,newlist,interval)


listword = list()
newlistword = list()

def newfunc(value,newlist,interval):
    print(value[int(interval[0])])
    intervalstart = int(interval[0])-1
    intervalend = int(interval[1])-1
    strfirst = value[intervalstart]
    strsecond = value[intervalend]
    if strfirst == newlist[1]:
        if strsecond != newlist[1]:
            newlistword.append(value)
        else:
            print(value)
    elif strsecond == newlist[1]:
        if strfirst != newlist[1]:
            newlistword.append(value)


    # enumerated = [place+1 for place, letter in enumerate(value) if letter == newlist[1]]
    # print(enumerated)
    # for v in enumerated:
    #     if v == int(interval[0]) or v == int(interval[1]):
    #         if v == int(interval[0]) and v == int(interval[1]):
    #             print(value)
    #         else:
    #             newlistword.append(value)




def func(y,newlist,interval):
    countedArray = {}
    for char in y:
        if char in countedArray:
                countedArray[char] += 1
        else:
                countedArray[char] = 1

    for k,v in countedArray.items():
        if k == newlist[1]:
            if v >= int(interval[0]) and v<= int(interval[1]):
               listword.append(y)




func0()

print(len(newlistword))
print(len(listword))