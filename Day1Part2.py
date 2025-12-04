dialValue = 50
count = 0

with open("inputday1part1.txt") as file:
    for line in file:
        first = line[0]
        num = int(line[1:])
        old = dialValue

        # apply movement
        if first == "R":
            dialValue += num
        else:
            dialValue -= num

        # count crossings of 0 during rotation
        diff = dialValue - old

        if diff > 0:  # moving right
            count += (old // 100) != (dialValue // 100)
        else:  # moving left
            # integer division for negatives is tricky → use abs
            count += (abs(old) // 100) != (abs(dialValue) // 100)

        # count multiple full wraps
        count += abs(diff) // 100

        # final landing check
        dialValue %= 100
        if dialValue == 0:
            count += 1

print(count)
