#Open file, separate into lines, convert each str line to int
file = open("Day-2-input.txt")
lines = file.readlines()

forward = 0
depth = 0
aim = 0

for line in lines:
    if "f" in line: #going forward (remove aim line for Part 1)
        for char in line:
            if char.isdigit():
                forward += int(char)
                depth = depth + (aim * int(char))
    elif "u" in line: #going up (remove aim, uncomment depth for Part 1)
        for char in line:
            if char.isdigit():
                #depth -= int(char)
                aim -= int(char)
    else: #going down (remove aim, uncomment depth for Part 1)
        for char in line:
            if char.isdigit():
                #depth += int(char)
                aim += int(char)

print(depth*forward)