# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3


def solution(n):
    count = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count  # is_prime 초기화 -> 소수가 아니면 !is_prime -> for문 break -> is_prime 초기화 ->
    # 소수면 count += 1
    # 프로그래머스 기준 최대 3000 ms


def solution1(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)  # 눈에 띄이는 답 (에라토스테네스의 체)
    # 프로그래머스 기준 최대 300 ms
