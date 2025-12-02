dialValue = 50
count = 0
with open("inputday1part1.txt") as file:
    for line in file:
        first = line[0]
        num = int(line[1:])
        if first == "R":
            dialValue = dialValue + num
        else:
            dialValue = dialValue - num
        dialValue = dialValue % 100
        if dialValue == 0:
            count = count + 1
print(count)