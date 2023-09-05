def day3_1():
    file = open('input.txt', 'r')
    data = file.read()

    history = [(0, 0)]

    for i in range(len(data)):
        last = history[-1]
        if data[i] == 'v':
            history.append((last[0], last[1]-1))
        elif data[i] == '^':
            history.append((last[0], last[1]+1))
        elif data[i] == '>':
            history.append((last[0]+1, last[1]))
        elif data[i] == '<':
            history.append((last[0]-1, last[1]))

    print(len(set(history)))


if __name__ == '__main__':
    day3_1()
