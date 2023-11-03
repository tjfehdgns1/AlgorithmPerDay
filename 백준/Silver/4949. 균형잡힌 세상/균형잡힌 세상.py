from sys import stdin
input = stdin.readline

while True:
    a = input().rstrip()

    if a == '.':
        break

    b = []
    bal = True
    for c in a:
        if c in '([':
            b.append(c)
        elif c in ')]':
            if not b or (c == ')' and b[-1] != '(') or (c == ']' and b[-1] != '['):
                bal = False
                break
            b.pop()
    if bal and not b:
        print('yes')
    else:
        print('no')