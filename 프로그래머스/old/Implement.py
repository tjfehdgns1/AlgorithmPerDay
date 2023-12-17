def CountThree():
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count += 1

    print(count)


def Knight():
    # Knight position
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord("a")) + 1

    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0

    for move in moves:
        next_row = row + moves[0]
        next_column = column + moves[1]

        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    print(result)


def StringSort():
    data = input()
    result = []
    value = 0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(value)

    print("".join(result))
