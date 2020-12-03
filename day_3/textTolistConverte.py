my_file = open('treeopensqure.txt')
all_the_lines = my_file.readlines()
items = []
for i in all_the_lines:
    s=i.split('\n')
    print(s[0])
    items.append(s[0])
print(len(items))
print(items)

# for case of 259 Right 3, down 1
#   64              Right 1, down 1
#    65 Right 5, down 1.
#59
#64

print(259 * 64 * 65 * 59 * 65 )

# Right 1, down 1.
#    Right 3, down 1. (This is the slope you already checked.)
#    Right 5, down 1.
#    Right 7, down 1.
#    Right 1, down 2.
