def solution(s):
    answer = []
    a = sorted(map(int, s.split()))
    answer.append(a[0])
    answer.append(a[-1])

    return " ".join(str(i) for i in answer)
