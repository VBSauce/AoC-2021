#Parse file into lines
with open("Day-3-input.txt") as f:
    lines = f.read().splitlines()

index = 0
gamma = []
eps = []

while index < len(lines[0]):
    ones = 0
    gamma_create = []
    for line in lines:
        gamma_create.append(line[index])
        if line[index] == '1':
            ones += 1
    index += 1

    if ones > len(gamma_create)/2:
        print("Ones!")
        gamma.append(1)
        eps.append(0)
        print(gamma)
        print(eps)
    else:
        print("Zeros!")
        gamma.append(0)
        eps.append(1)
    print(gamma)
    print(eps)

gamma_bin = "".join(map(str, gamma))
gamma_dec = int(gamma_bin, 2)
eps_bin = "".join(map(str, eps))
eps_dec = int(eps_bin, 2)
print(gamma_dec * eps_dec)