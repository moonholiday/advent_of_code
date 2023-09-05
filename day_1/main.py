file = open('input.txt', 'r')
data = file.read()


def day1_1():

    floor = 0

    for char in data:
        if (char == "("):
            floor += 1
        elif (char == ")"):
            floor -= 1
    print(floor)


def day1_2():
    floor = 0
    position = 0
    for char in data:
        position += 1
        if (char == "("):
            floor += 1
            if (floor == -1):
                break
        elif (char == ")"):
            floor -= 1
            if (floor == -1):
                break
    print(position)


if __name__ == '__main__':
    day1_1()
    day1_2()
