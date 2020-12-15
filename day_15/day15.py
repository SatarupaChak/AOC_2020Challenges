arr = [1,0,16,5,17,4]
finallist = list()
turnNumber = 1
turndictionary = {}

for x in arr:
    turndictionary[turnNumber] = x
    turnNumber = turnNumber +1
print(turndictionary)

turndictionary[7]=0

for i in range(8,30000001):
    numberToTest = turndictionary[i-1]
    arr = [i for i, j in turndictionary.items() if j == numberToTest]
    print(arr)
    if len(arr)>=2:
        newVAl = arr[len(arr)-1]-arr[len(arr)-2]
        turndictionary[i] = newVAl
        continue
    else:
        turndictionary[i] = 0
        continue
print(turndictionary)



