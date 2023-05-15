def ricecake(N, M, given) :
    first, last = min(given)-M, max(given)
    
    answer = 0
    while(first <= last) :
        total = 0
        mid = (first+last) // 2
        # 떡이 나오면 잘린 길이 저장
        for num in given :
            if num > mid :
                total += num - mid
        # 잘린 길이의 합이 M보다 작으면 오른쪽 반절 없앰
        if total < M :
            last = mid - 1
        # 잘린 길이의 합이 M보다 크거나 같으면 최적화된 답 answer에 저장하고 왼쪽 반절 없앰
        else :
            answer = mid
            first = mid + 1
            
    return answer

N = 4
M = 6
given = [19, 15, 10, 17]
result = ricecake(N, M, given)
