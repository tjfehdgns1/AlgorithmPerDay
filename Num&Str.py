#문제 설명

#네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

#다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

#1478 → "one4seveneight"
#234567 → "23four5six7"
#10203 → "1zerotwozero3"
#이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

#참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

#숫자	영단어
#0	zero
#1	one
#2	two
#3	three
#4	four
#5	five
#6	six
#7	seven
#8	eight
#9	nine

def solution(s):
    m = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4,
         'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' :9,}
    for char in m.keys() :
        if char in s :
            s.replace(char, str(m[char]))
    return s # 문자열은 immutable(불변)한 자료형이기 때문에 replace() 메서드로 변경할 수 없음. 따라서 replace() 메서드를 호출하여도 실제로는 s의 내용이 변경안됨

def solution(s):
    m = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4',
         'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' :'9'}
    for char in m.keys():
        if char in s:
            idx = s.find(char)
            s = s[:idx] + m[char] + s[idx+len(char):]
    return int(s) # 런타임 에러

def solution(s):
    nums = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ""
    temp = ""

    for c in s:
        if c.isdigit():
            answer += c
        else:
            temp += c
            if temp in nums:
                answer += nums[temp]
                temp = ""

    return int(answer) # 문자는 따로 뺴서 dic 확인후 value를 넣은 다름 초기화


num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer) # 깔끔

def solution(s):
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    for i, c in enumerate(nums) :
        s =  s.replace(c,str(i))
    return int(s) # enumerate로 수정
