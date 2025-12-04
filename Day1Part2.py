dial = 50        # starting position
count = 0        # number of times a click lands on 0

with open("inputday1part1.txt") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        first = line[0]
        steps = int(line[1:])

        pos = dial % 100

        rotations = steps // 100
        count += rotations
        residue = steps % 100

        if first == "R":

            if residue > 0 and pos != 0 and pos + residue >= 100:
                count += 1

            dial = (pos + residue) % 100

        else: 
            if residue > 0 and pos != 0 and pos - residue <= 0:
                count += 1

            dial = (pos - residue) % 100

print(count)
