'''숫자 짝꿍
문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

제한사항
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
X, Y는 0으로 시작하지 않습니다.
X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
입출력 예
X	    Y	        result
"100"	"2345"	    "-1"
"100"	"203045"	"0"
"100"	"123450"	"10"
"12321"	"42531"	    "321"
"5525"	"1255"	    "552"'''


def solution(X, Y):
    intersect = list(set(X) & set(Y))
    pair = []
    for num in intersect:
        x_count = X.count(num)
        y_count = Y.count(num)
        pair_count = min(x_count, y_count)
        for _ in range(pair_count):
            pair.append(str(num))
    pair.sort(reverse=True)

    if not pair:
        return "-1"
    elif len(pair) == pair.count("0"):
        return "0"
    else:
        return "".join(pair)


# 691.79ms 48분
# 교집합 구하고 겹치는 수 최소값 만큼 pair에 넣어줌


def solution(X, Y):
    answer = ""

    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))

    if answer == "":
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return answer  # 간결한 코드 85.91ms
    # sort를 쓰지 않기 위해 큰수부터 range
