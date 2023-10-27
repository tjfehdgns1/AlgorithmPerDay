def UntilOne() :
    n, k = map(int, input().split())

    result = 0

    while True :
        target = (n // k) * k
        result += (n - target)

        if n <k :
            break

    result += 1 
    n //= k

    result += (n - 1)
    print(result)


def MultiOrAdd() :
    data = input()

    result = int(data[0])

    for i in range(1, len(data)) :
        num = int(data[i])
        if num <= 1 or result <= 1 :
            result += num
        else :
            result *= num

    print(result) 

def Fear() :
    num = int(input())
    fear = list(map(int, input().split())) if len(map(input().split())) == int(num) else "다시 입력해라"
    count = 0
    group = 0
    fear.sort()

    for num in fear :
        count += 1
        if count >= num :
            group += 1
            count = 0
        
        
    print(group)