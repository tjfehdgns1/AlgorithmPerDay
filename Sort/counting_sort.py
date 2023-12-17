array = [0, 1, 5, 3, 2, 1, 1, 6, 7, 9, 7, 0]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
