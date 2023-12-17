"""최빈값 구하기
문제 설명
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

제한사항
0 < array의 길이 < 100
0 ≤ array의 원소 < 1000
입출력 예
array	            result
[1, 2, 3, 3, 3, 4]	3
[1, 1, 2, 2]	    -1
[1]	                1"""


def solution(array):
    dic = {}

    for set_num in list(set(array)):
        cnt = array.dic(set_num)

        if cnt in dic.keys():
            dic[cnt].append(set_num)
        else:
            dic[cnt] = [set_num]

    max_num = dic[max(dic.keys())]

    if len(max_num) == 1:
        return max_num[0]
    else:
        return -1  # ex) dic == {1: [1, 2, 4], 3: [3]}


#################################################
def solution1(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1  # 다른 사람 답변,


# 이함수는 만약 array가 []일때 -1을 return 하지만 solution은 딕셔너리가 null이라서 예외처리를 해야함
##########################
def solution2(array):
    dic = {}

    for set_num in list(set(array)):
        cnt = array.dic(set_num)

        if cnt in dic.keys():
            dic[cnt].append(set_num)
        else:
            dic[cnt] = [set_num]
    if dic:
        max_num = dic[max(dic.keys())]
    else:
        return -1
    if len(max_num) == 1:
        return max_num[0]
    else:
        return -1  # 예외 처리를 통해 solution1과 같이 동작하도록 함
