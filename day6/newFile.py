charlist = list()
finalCount = 0
with open('test.txt') as inline:
    for x in inline.readlines():
        cntr = 0
        if x != '\n':
            newSet = set(x.rstrip('\n'))
            charlist.append(newSet)
            cntr += 1

        elif x == '\n':
            charset = charlist[0]
            for x in range(1, len(charlist)):
                charset = charset.intersection(charlist[x])
            print(charset)
            print(len(charset))
            finalCount += len(charset)
            charlist.clear()

print(finalCount)
