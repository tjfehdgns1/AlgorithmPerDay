def solution(citations):
    n = len(citations)
    citations.sort()
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0
