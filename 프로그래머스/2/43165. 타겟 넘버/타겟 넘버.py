def dfs(numbers, target, current, index):
    if index == len(numbers):
        return 1 if current == target else 0

    return dfs(numbers, target, current + numbers[index], index + 1) + dfs(
        numbers, target, current - numbers[index], index + 1
    )


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
