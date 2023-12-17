"""가까운 수
문제 설명
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ array의 길이 ≤ 100
1 ≤ array의 원소 ≤ 100
1 ≤ n ≤ 100
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
입출력 예
array	        n	result
[3, 10, 28]	    20	28
[10, 11, 12]	13	12"""


def solution(array, n):
    closest = array[0]
    for num in array:
        if abs(num - n) < abs(closest - n):
            closest = num
        elif abs(num - n) == abs(closest - n) and num < closest:
            closest = num
    return closest  # 문제를 읽고 그래로 푼듯한 풀이


###
def solution1(array, n):
    array.sort(key=lambda x: (abs(x - n), x - n))
    answer = array[0]
    return answer  # key sort를 이용하여 구하기, 튜플을 사용한 이유는 절댓값이 같지떄 작은 x를 구할려고
