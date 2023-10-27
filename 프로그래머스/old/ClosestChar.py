#가장 가까운 같은 글자
#문제 설명
#예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

#b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
#a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
#n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
#a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
#n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
#a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
#따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

#문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.

#제한사항
#1 ≤ s의 길이 ≤ 10,000
#s은 영어 소문자로만 이루어져 있습니다.
#입출력 예
#s	result
#"banana"	[-1, -1, -1, 2, 2, 2]
#"foobar"	[-1, -1, 1, -1, -1, -1]

def solution(s):
    a = []
    for i, char in enumerate(s) :
        if char in s[:i] :
            a.append('-1')
        if char in s[:i] and s[:i].count(char) > 1 :
            pass
    return a # 못풀음

def solution(s):
    answer = [] # 정답을 담을 리스트
    chars = [0] * 26 # 각 알파벳의 등장 위치를 담을 리스트

    for i in range(len(s)):
        c = ord(s[i]) - ord('a') # 현재 문자의 인덱스 계산
        if chars[c] == 0: # 이전에 등장한 적이 없는 문자인 경우
            answer.append(-1) # -1을 정답 리스트에 추가
        else: # 이전에 등장한 적이 있는 문자인 경우
            min_distance = i - chars[c] # 가장 가까운 등장 위치 계산
            answer.append(min_distance)
        chars[c] = i # 현재 문자의 등장 위치를 업데이트
    return answer #런타임 에러

def solution(s):
    answer = []
    chars = {}

    for i in range(len(s)):
        c = s[i]
        if c not in chars:
            chars[c] = i
            answer.append(-1)
        else:
            min_distance = i - chars[c]
            for j in range(chars[c]+1, i):
                if s[j] == c:
                    min_distance = min(min_distance, i-j)
                    break
            chars[c] = i
            answer.append(min_distance)

    return answer # 해결

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

