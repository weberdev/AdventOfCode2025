dialValue = 50
count = 0
with open("inputday1part1.txt") as file:
    for line in file:
        first = line[0]
        num = int(line[1:])
        pos = dialValue
        old = pos
        if first == "R":
            dialValue = dialValue + num
            if dialValue >= 100:
                rotation = dialValue // 100
                count = count + rotation
        else:
            dialValue = dialValue - num
            if dialValue <= 0:
                rotation = abs(dialValue // 100)
                count = count + rotation
        dialValue = dialValue % 100
print(count)