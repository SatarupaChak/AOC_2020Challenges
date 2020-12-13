directionlist = ['N1', 'R90', 'S5', 'R180', 'N3', 'W1', 'L180', 'F92', 'R270', 'E4', 'F4', 'W4', 'W4', 'L180', 'S2',
                 'W2', 'F90', 'E1', 'S5', 'W3', 'F78', 'S5', 'R180', 'F100', 'N1', 'W3', 'L90', 'L90', 'N1', 'F94',
                 'W2', 'R90', 'F49', 'W2', 'F26', 'R180', 'W1', 'S5', 'R180', 'W4', 'S3', 'R90', 'W3', 'S4', 'E5', 'S1',
                 'F13', 'N5', 'R270', 'E2', 'R270', 'S5', 'F3', 'E3', 'F4', 'S3', 'R270', 'S1', 'W4', 'R90', 'S4',
                 'L180', 'N4', 'F81', 'W2', 'R90', 'F61', 'R90', 'F13', 'N3', 'R180', 'W1', 'F98', 'S5', 'F50', 'W5',
                 'S3', 'W5', 'R90', 'F17', 'S5', 'F70', 'F7', 'E2', 'F87', 'E1', 'L270', 'F59', 'E2', 'R180', 'N5',
                 'F59', 'L90', 'N5', 'W5', 'F10', 'N3', 'E1', 'R90', 'W1', 'S2', 'R90', 'N5', 'F25', 'R90', 'E2', 'F57',
                 'R180', 'E1', 'N3', 'W2', 'F85', 'L90', 'F50', 'W2', 'R90', 'S3', 'R90', 'F27', 'E1', 'S1', 'L90',
                 'F32', 'L90', 'W3', 'R90', 'E1', 'F39', 'S5', 'E4', 'F50', 'W4', 'L90', 'F63', 'N2', 'F67', 'W3',
                 'R90', 'F4', 'N2', 'R90', 'F90', 'N5', 'L180', 'F24', 'E5', 'N3', 'L180', 'F67', 'E3', 'L90', 'S3',
                 'F49', 'R90', 'E5', 'F89', 'W5', 'F62', 'F39', 'F33', 'W1', 'R90', 'F18', 'S3', 'R90', 'N4', 'F47',
                 'N5', 'N3', 'W2', 'S5', 'L90', 'E4', 'L90', 'W2', 'R90', 'W5', 'L90', 'W5', 'N4', 'F64', 'R90', 'S2',
                 'W4', 'R90', 'N3', 'F18', 'L90', 'S4', 'L90', 'F31', 'S4', 'L90', 'F79', 'R90', 'F69', 'N3', 'E4',
                 'F64', 'N2', 'E4', 'R90', 'F20', 'R180', 'E1', 'F85', 'W1', 'S5', 'S2', 'F21', 'R90', 'F43', 'N1',
                 'F18', 'S5', 'R180', 'F52', 'L180', 'W4', 'F5', 'L90', 'F70', 'S4', 'N3', 'R180', 'F64', 'R90', 'F17',
                 'R90', 'E5', 'F85', 'N1', 'F74', 'E5', 'F21', 'N1', 'F35', 'N1', 'F65', 'W2', 'F67', 'N1', 'E5', 'F79',
                 'S4', 'R90', 'F20', 'R180', 'W5', 'L180', 'S4', 'F56', 'S4', 'L90', 'E5', 'F13', 'S5', 'F38', 'W1',
                 'S2', 'L90', 'N4', 'E3', 'R180', 'W3', 'N1', 'R90', 'F52', 'N5', 'F23', 'E5', 'F82', 'E5', 'S2', 'E3',
                 'N3', 'S2', 'L90', 'N1', 'R90', 'S5', 'F60', 'W1', 'N2', 'W1', 'N3', 'E4', 'F2', 'E2', 'L90', 'S1',
                 'L90', 'E4', 'N1', 'R180', 'E2', 'R180', 'F93', 'F94', 'L90', 'S4', 'E5', 'R90', 'F5', 'S2', 'E2',
                 'S3', 'E4', 'R180', 'F56', 'E2', 'N2', 'F3', 'R90', 'W2', 'F94', 'W5', 'F47', 'L180', 'F68', 'E5',
                 'F63', 'S3', 'E4', 'F93', 'L90', 'S5', 'L180', 'W5', 'S5', 'W3', 'L180', 'F34', 'R90', 'F87', 'W4',
                 'S1', 'W3', 'R270', 'S1', 'E1', 'F78', 'E4', 'R90', 'F91', 'W4', 'S3', 'W1', 'F41', 'N4', 'E1', 'F66',
                 'S1', 'W5', 'F62', 'N2', 'W2', 'L90', 'W1', 'F23', 'L270', 'N2', 'W2', 'S3', 'F9', 'R90', 'F2', 'E4',
                 'F61', 'L90', 'W5', 'N4', 'F97', 'L90', 'F93', 'N5', 'L270', 'R90', 'W1', 'R90', 'R90', 'N4', 'E1',
                 'F72', 'N4', 'R270', 'F24', 'W1', 'F79', 'S1', 'E3', 'N4', 'E3', 'L90', 'W2', 'S1', 'R270', 'W5',
                 'F24', 'E5', 'S4', 'F22', 'L180', 'F57', 'S5', 'R90', 'N4', 'W3', 'F18', 'N2', 'R90', 'E3', 'F55',
                 'N2', 'R90', 'S5', 'F4', 'W3', 'L90', 'N2', 'W3', 'L270', 'E4', 'R90', 'F46', 'S5', 'N1', 'F16', 'N1',
                 'R90', 'F8', 'L180', 'N2', 'W3', 'N4', 'E1', 'S3', 'L90', 'F4', 'E5', 'N5', 'E3', 'R90', 'F35', 'N2',
                 'F68', 'F33', 'E5', 'F38', 'E4', 'F27', 'R180', 'S5', 'F47', 'R90', 'F43', 'R90', 'S1', 'F84', 'L180',
                 'F47', 'R90', 'N4', 'E4', 'F77', 'R180', 'N1', 'E2', 'S4', 'F45', 'S1', 'L90', 'E5', 'F40', 'L90',
                 'W5', 'F25', 'W4', 'R90', 'F80', 'N5', 'E2', 'F74', 'W3', 'N3', 'E4', 'F48', 'N3', 'R90', 'N2', 'W1',
                 'L90', 'S2', 'F35', 'L90', 'E5', 'R180', 'W5', 'N2', 'E1', 'L90', 'N2', 'F78', 'S5', 'R270', 'S5',
                 'R90', 'N5', 'E3', 'L90', 'S5', 'F13', 'S5', 'F52', 'L90', 'N2', 'R180', 'E1', 'F41', 'S1', 'F20',
                 'N4', 'F34', 'N2', 'F45', 'E5', 'L90', 'W3', 'L270', 'N5', 'F52', 'R90', 'N5', 'E5', 'N2', 'W2', 'W5',
                 'R270', 'W5', 'F10', 'N3', 'F63', 'N4', 'F53', 'L90', 'E5', 'L270', 'F17', 'N1', 'L90', 'F26', 'F93',
                 'R90', 'S5', 'R270', 'S5', 'R180', 'N4', 'F58', 'L180', 'F40', 'S2', 'F54', 'N5', 'F70', 'W1', 'N4',
                 'W1', 'L90', 'W5', 'R90', 'N2', 'R90', 'S5', 'F95', 'W4', 'L180', 'E3', 'F68', 'S1', 'F56', 'R90',
                 'W1', 'L180', 'F66', 'R90', 'S2', 'F57', 'L90', 'E1', 'F42', 'S4', 'F44', 'L90', 'F42', 'E4', 'R90',
                 'S4', 'W5', 'R90', 'E4', 'S4', 'E5', 'F27', 'R90', 'N1', 'R90', 'E5', 'R90', 'W4', 'S1', 'F81', 'N5',
                 'R180', 'S4', 'E4', 'F68', 'S3', 'L90', 'E4', 'E4', 'L180', 'E3', 'F8', 'W2', 'L90', 'S4', 'L180',
                 'N2', 'L180', 'E1', 'R90', 'W5', 'N4', 'W4', 'R90', 'F1', 'S5', 'E2', 'L90', 'F49', 'N4', 'W3', 'R90',
                 'E5', 'F33', 'R180', 'S4', 'E5', 'S2', 'F79', 'W4', 'F38', 'R90', 'F1', 'L90', 'F56', 'L270', 'N2',
                 'L90', 'E2', 'L90', 'F25', 'W1', 'S4', 'L270', 'W3', 'R90', 'N2', 'F68', 'E1', 'R180', 'W3', 'R90',
                 'W3', 'R90', 'S3', 'F4', 'W3', 'N3', 'R90', 'W3', 'N1', 'F54', 'W2', 'S5', 'E4', 'F76', 'F47', 'N1',
                 'F32', 'L180', 'L90', 'F19', 'N2', 'E5', 'L90', 'E1', 'L90', 'E3', 'R90', 'F48', 'R270', 'S3', 'R180',
                 'S4', 'F53', 'R90', 'F90', 'E4', 'F100', 'L90', 'F49', 'N1', 'W1', 'F56', 'E2', 'N5', 'L90', 'F39',
                 'R90', 'W2', 'F26', 'E4', 'N4', 'L90', 'F9', 'L90', 'F41', 'W5', 'N4', 'S1', 'W4', 'N3', 'R90', 'N5',
                 'L270', 'F82', 'L90', 'F75', 'S5', 'F25', 'S4', 'F67', 'N4', 'F57', 'E4', 'N4', 'F73', 'W5', 'L90',
                 'E2', 'R180', 'N5', 'L270', 'W3', 'F95', 'W2', 'S4', 'E1', 'R180', 'N3', 'W2', 'N1', 'F28', 'N2',
                 'R90', 'E3', 'S1', 'F41', 'E4', 'N1', 'R90', 'F12', 'L90', 'N2', 'S2', 'E3', 'F31', 'W1', 'L90', 'E5',
                 'S1', 'F12', 'R180', 'W5', 'R90', 'F26']

direction = ''
amount = 0
corordinatex = 'east'
amountx = 0
corordinatey = 'north'
amounty = 0
temp = ''


def getfromlist():
    for x in directionlist:
        if len(x) == 3:
            direction = x[:1]
            amount = int(x[1:3])
            if direction == 'R':
                temp = getR(amount)

            elif direction == 'L':
                temp = getL(amount)


            elif direction == 'N':

                getN(amount, corordinatey, amounty)

            elif direction == 'S':

                getS(amount, corordinatey, amounty)

            elif direction == 'W':

                getW(amount, corordinatey, amounty)

            elif direction == 'E':

                getE(amount, corordinatey, amounty)

            elif direction == 'F':

                getF(amount, corordinatey, amounty)

        elif len(x) == 2:
            direction = x[:1]
            amount = int(x[1:2])
            if direction == 'R':
                temp = getR(amount)

            elif direction == 'L':
                temp = getL(amount)

            elif direction == 'N':
                getN(amount, corordinatey, amounty)
            elif direction == 'S':
                getS(amount, corordinatey, amounty)
            elif direction == 'W':
                getW(amount, corordinatey, amounty)
            elif direction == 'E':
                getE(amount, corordinatey, amounty)
            elif direction == 'F':
                getF(amount, corordinatey, amounty)
        elif (len(x)) == 4:
            direction = x[:1]
            amount = int(x[1:4])
            if direction == 'R':
                temp = getR(amount)

            elif direction == 'L':
                temp = getL(amount)


            elif direction == 'N':

                getN(amount, corordinatey, amounty)

            elif direction == 'S':

                getS(amount, corordinatey, amounty)

            elif direction == 'W':

                getW(amount, corordinatey, amounty)

            elif direction == 'E':

                getE(amount, corordinatey, amounty)

            elif direction == 'F':

                getF(amount, corordinatey, amounty)




def getN(amount, corordinatey, amounty, ):
    if corordinatey == 'south':
        corordinatey = 'north'
        newamt = amount - amounty
        amounty = newamt
        return amounty

    elif corordinatey == 'north':
        newamt = amount + amounty
        amounty = newamt
        return amounty


def getW(amount, corordinatey, amounty):
    if corordinatey == 'west':
        newamt = amount + amounty
        amounty = newamt
        return amounty
    elif corordinatey == 'east':
        corordinatey = 'west'
        newamt = amount - amounty
        amounty = newamt
        return amounty


def getE(amount, corordinatey, amounty):
    if corordinatey == 'east':
        newamt = amount + amounty
        amounty = newamt
        return amounty
    elif corordinatey == 'west':
        corordinatey = 'east'
        newamt = amount - amounty
        amounty = newamt
        return amounty


def getF(amount, corordinatey, amounty):
    if corordinatey == 'east':
        print("face")


def getS(amount, corordinatey, amounty):
    if corordinatey == 'north':
        corordinatey = 'south'
        newamt = amount - amounty
        amounty = newamt
        return amounty, corordinatey
    elif corordinatey == 'south':
        newamt = amount + amounty
        amounty = newamt
        return amounty, corordinatey


def getR(amount):
    tempCoordinate = ''
    if corordinatex == 'east':
        if amount <= 90 and amount < 180:
            tempCoordinate = "south"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "west"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "north"

        elif amount == 360:
            tempCoordinate = "east"

    elif corordinatex == 'west':
        if amount <= 90 and amount < 180:
            tempCoordinate = "north"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "east"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "south"

        elif amount == 360:
            tempCoordinate = "west"

    elif corordinatex == 'north':
        if amount <= 90 and amount < 180:
            tempCoordinate = "east"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "south"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "west"

        elif amount == 360:
            tempCoordinate = "north"

    elif corordinatex == 'south':
        if amount <= 90 and amount < 180:
            tempCoordinate = "west"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "north"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "east"

        elif amount == 360:
            tempCoordinate = "south"

    return tempCoordinate


def getL(amount):
    tempCoordinate = ''
    if corordinatex == 'east':
        if amount <= 90 and amount < 180:
            tempCoordinate = "north"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "west"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "south"

        elif amount == 360:
            tempCoordinate = "east"

    elif corordinatex == 'west':
        if amount <= 90 and amount < 180:
            tempCoordinate = "south"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "east"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "north"

        elif amount == 360:
            tempCoordinate = "west"

    elif corordinatex == 'north':
        if amount <= 90 and amount < 180:
            tempCoordinate = "west"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "south"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "east"

        elif amount == 360:
            tempCoordinate = "north"

    elif corordinatex == 'south':
        if amount <= 90 and amount < 180:
            tempCoordinate = "east"
        elif amount >= 180 and amount < 270:
            tempCoordinate = "north"

        elif amount >= 270 and amount < 360:
            tempCoordinate = "west"

        elif amount == 360:
            tempCoordinate = "south"

    return tempCoordinate


getfromlist()
