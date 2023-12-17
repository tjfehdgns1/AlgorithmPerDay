def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)


n = int(input())
sequence = list(map(int, input().split()))

result = longest_increasing_subsequence(sequence)
print(result)
