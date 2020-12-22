playerOne = [18, 19, 16, 11, 47, 38, 6, 27, 9, 22, 15, 42, 3, 4, 21, 41, 14, 8, 23, 30, 40, 13, 35, 46, 50]
playerTwo = [39, 1, 29, 20, 45, 43, 12, 2, 37, 33, 49, 32, 10, 26, 36, 17, 34, 44, 25, 28, 24, 5, 48, 31, 7]

# with open('somfile.txt') as player_1:
#      for x in player_1.readlines():
#          if x.rstrip('\n') != 'Player 1:':
#              playerOne.append(int(x.rstrip('\n')))
#







# print(playerOne)
#
# with open('someOtherfile.txt') as player_2:
#     for y in player_2.readlines():
#          if y.rstrip('\n') != 'Player 2:':
#               playerTwo.append(int(y.rstrip('\n')))
#
#
# print(playerTwo)

k= 0

while k <= 1000:

  if len(playerOne) > 0 and len(playerTwo)>0:
     print(playerOne[0], playerTwo[0])
     if playerOne[0] > playerTwo[0]:
            playerOne.insert(len(playerOne),playerOne[0])
            playerOne.insert(len(playerOne),playerTwo[0])
            playerOne.remove(playerOne[0])
            playerTwo.remove(playerTwo[0])



     elif playerTwo[0] >playerOne[0]:
            playerTwo.insert(len(playerTwo), playerTwo[0])
            playerTwo.insert(len(playerTwo), playerOne[0])
            playerOne.remove(playerOne[0])
            playerTwo.remove(playerTwo[0])

  else:
      print(playerOne,playerTwo)

  k = k + 1

finalArr = [47, 26, 34, 15, 45, 38, 42, 11, 27, 7, 18, 4, 35, 31, 39, 32, 19, 1, 8, 5, 40, 23, 30, 17, 46, 21, 37, 13, 43, 12, 29, 10, 33, 3, 14, 2, 50, 20, 28, 16, 44, 41, 49, 25, 48, 6, 36, 22, 24, 9]
sum = 0
i=0
for x in finalArr:
    print(len(finalArr))
    multi = x * (len(finalArr)-i)
    sum= sum+multi
    i= i+1

print(sum)




