#Parse file into lines
with open("Day-3-input.txt") as f:
    lines = f.read().splitlines()

#Get the first char of each line
#compare 1's to 0's, divide into lists
#compare list lengths, grab right list, reinsert through loop

index = 0
oxygen = lines
co2 = lines

#oxygen loop
while index < len(lines[0]) and len(oxygen) > 1:
    current_bit_0 = []
    current_bit_1 = []
    for line in oxygen:
        if line[index] == '0':
            current_bit_0.append(line)
        else:
            current_bit_1.append(line)

    if len(current_bit_1) >= len(current_bit_0):
        oxygen = current_bit_1
    else:
        oxygen = current_bit_0

    index += 1

#co2 loop
index = 0
while index < len(lines[0]) and len(co2) > 1:
    current_bit_0 = []
    current_bit_1 = []
    for line in co2:
        if line[index] == '0':
            current_bit_0.append(line)
        else:
            current_bit_1.append(line)

    if len(current_bit_0) <= len(current_bit_1):
        co2 = current_bit_0
    else:
        co2 = current_bit_1

    index += 1

oxygen_bin = str(oxygen[0])
oxygen_dec = int(oxygen_bin, 2)
co2_bin = str(co2[0])
co2_dec = int(co2_bin, 2)

print(co2_dec * oxygen_dec)