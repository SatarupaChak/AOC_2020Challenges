from itertools import permutations
arr = [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]
p =0


while p < (len(arr)-3):
    val1 = arr[p]
    val2 = arr[p+1]
    val3=arr[p+2]
    val4= arr[p+3]
    if val4- val1 == 3 or val4-val2:
        print("another arrangement")

    elif val4-val1==1or val4- val2:
        print("another arrangement")

    p=p+1
cntr = 0
for p in permutations(arr):
    cntr = cntr+1

print(cntr)