#Open file, separate into lines, convert each str line to int
file = open("input.txt")
lines = file.readlines()
lines = [int(i) for i in lines]

#PART 1
base = 0
increase = 0

for line in lines:
    line = int(line)
    #Stop first iteration from incrementing increase
    if base == 0:
        base = line
    elif line > base:
        increase += 1
    base = line

print(increase)
'''
PART 2
increase = 0

#get index of items, not item itself
for x in range(len(lines)-3):
    sum_1 = lines[x] + lines[x + 1] + lines[x + 2]
    sum_2 = lines[x + 3] + lines[x + 1] + lines[x + 2]
    if sum_2 > sum_1:
        increase += 1
print(increase)
'''