#Trying out map

measure = list(map(int, open("input.txt")))


'''
MY DEFAULT OPENER CODE
file = open("input.txt")
lines = file.readlines()
lines = [int(i) for i in lines]
'''
'''
PART 2
increase = 0
for x in range(len(lines)-3):
    sum_1 = lines[x] + lines[x + 1] + lines[x + 2]
    sum_2 = lines[x + 3] + lines[x + 1] + lines[x + 2]
    if sum_2 > sum_1:
        increase += 1
print(increase)
'''
'''
PART 1
base = 0
increase = 0

for line in lines:
    line = int(line)
    if base == 0:
        base = line
    elif line > base:
        increase += 1
    base = line
    print(f"base is {base}, line is {line}, increase is {increase}")

print(increase)
'''
