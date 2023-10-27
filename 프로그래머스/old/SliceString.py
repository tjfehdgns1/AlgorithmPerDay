'''문자열 나누기
문제 설명
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.

제한사항
1 ≤ s의 길이 ≤ 10,000
s는 영어 소문자로만 이루어져 있습니다.
입출력 예
s	                result
"banana"	        3
"abracadabra"	    6
"aaabbaccccabba"	3'''
def solution(s) : 
    count = 0
    def cut(s):
        x = 1
        nonlocal count
        if s != '' :
            for i, char in enumerate(s[1:]) :
                if char == s[0] :
                    x += 1
                if x == (i+2-x) :
                    count += 1
                    return cut(s[i+2:])
            return s     
        else :
            return count   
    return count  #null

s = "banana"
result = solution(s)
print(result)


def solution(s):
    count = 0
    def cut(s):
        nonlocal count
        x = 1
        if len(s) == 1 :
            return count + 1
        if s:
            for i, char in enumerate(s[1:]):
                if char == s[0]:
                    x += 1
                if x == (i+2-x) :
                    count += 1
                    print(count)
                    return cut(s[i+2:])
            return s
        
        else:
            return count
    return cut(s) # 테스트 실패 1시간


def solution(s) :
    count = 0
    while s :
        x = 1
        for i, char in enumerate(s[1:]) :
                if char == s[0] :
                    x += 1
                if x == (i+2-x) :
                    count += 1
                    s = s[i+2:]
                    break
    return count # 10초 초과

def solution(s) :
    count = 0
    while s :
        x = 1
        if len(s) == 1 :
            count += 1
            break
        for i, char in enumerate(s[1:]) :
                if char == s[0] :
                    x += 1
                if x == (i+2-x) :
                    count += 1
                    s = s[i+2:]
                    break
    return count # 시간 초과

def solution(s) :
    count = 0
    l, r = 0 ,0
    for char in s :
        if l == r :
            count += 1
            k = char
        if k == char :
            l += 1
        else :
            r += 1
    return count