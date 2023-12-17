n = int(input())

given = [int(input()) for _ in range(n)]
stack = []
result = []
current = 1
flag = False
for i in given:
    while current <= i:
        result.append("+")
        stack.append(current)
        current += 1

    if stack[-1] == i:
        result.append("-")
        stack.pop()

    else:
        print("NO")
        flag = True
        break

if not flag:
    for i in result:
        print(i)
