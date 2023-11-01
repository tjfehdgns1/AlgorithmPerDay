from sys import stdin
input = stdin.readline

n = int(input())

a = []
for _ in range(n):
    b = input().split()
    match b[0]:
            case '1':
                a.append(int(b[-1]))
            case '2':
                if a:
                    print(a.pop())
                else:
                    print(-1)
            case '3':
                print(len(a))
            case '4':
                if a:
                    print(0)
                else:
                    print(1)
            case '5':
                if a:
                    print(a[-1])
                else:
                    print(-1)
            