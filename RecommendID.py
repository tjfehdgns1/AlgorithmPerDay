'''신규 아이디 추천
문제 설명
카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 
카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. 
"네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 
입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
다음은 카카오 아이디의 규칙입니다.

아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 
규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
신규 유저가 입력한 아이디가 new_id 라고 한다면,

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, 
new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
예를 들어, new_id 값이 "...!@BaT#*..y.abcdefghijklm" 라면, 
위 7단계를 거치고 나면 new_id는 아래와 같이 변경됩니다.

1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀌었습니다.
"...!@BaT#*..y.abcdefghijklm" → "...!@bat#*..y.abcdefghijklm"

2단계 '!', '@', '#', '*' 문자가 제거되었습니다.
"...!@bat#*..y.abcdefghijklm" → "...bat..y.abcdefghijklm"

3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
"...bat..y.abcdefghijklm" → ".bat.y.abcdefghijklm"

4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.
".bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.
"bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.
"bat.y.abcdefghijklm" → "bat.y.abcdefghi"

7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.
"bat.y.abcdefghi" → "bat.y.abcdefghi"

따라서 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 
네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi" 입니다.

[문제]
신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, 
"네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
new_id는 길이 1 이상 1,000 이하인 문자열입니다.
new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.

[입출력 예]
no	new_id	                        result
예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	                    "z--"
예3	"=.="	                        "aaa"
예4	"123_.def"	                    "123_.def"
예5	"abcdefghijklmn.p"	            "abcdefghijklmn"'''


def solution(new_id):
    # 1
    step_one = new_id.lower()
    step_two = []
    step_three = []
    step_five = []
    step_six = []
    print(step_one)
    # 2
    for char in step_one:
        if char == '-' or char == '_' or char == '.' or char.isdigit() or char.isalpha():
            step_two += char
    print(step_two)
    # 3 
    for i, char in enumerate(step_two):
        if i > 0 and char == '.' and step_two[i] == step_two[i-1]:
            continue
        step_three.append(char)
    print(step_three)
    # 4
    if step_three and step_three[-1] == '.':
        step_three.pop()
    if step_three and step_three[0] == '.':
        step_three.pop(0)
    print(step_three)
    # 5
    if len(step_three) == 0 :
        step_five.append('a')
    else :
        step_five = step_three
    # 6 
    if len(step_five) > 15:
        step_six = step_five[:15]
        if step_six[-1] == '.':
            step_six.pop()
    else:
        step_six = step_five
            
    print(step_six)
    # 7
    while len(step_six) < 3:
        step_six.append(step_six[-1])
    return "".join(step_six) # 1hour , 최대 0.50ms
# 규칙
# 3자 이상 15자 이하
# 소문자, 숫자, -, _, . 만 이용가능
# 마침표 중복 X, 처음끝 X

# 1. lower()
# 2. 규칙에 어긋하는 문자 제거
# 3. 중복 마침표 하나로
# 4. 마침표 처음 끝 제거
# 5. 빈 문자열 -> 'a'
# 6. 15자 넘어가면 [:15] 만약 마침표 끝에 있으면 제거
# 7. 2자 이하면  while len(id) < 3
##################################################

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st # 다른 사람 답변 (정규식), 최대 0.51ms

'''특성상 일정한 규칙을 가진 텍스트 문자열을 사용하는 경우가 많은데, 이럴 때 정규 표현식을 사용한다
메타 문자로 된 자원을 찾아야 하는 경우에는 다른 언어와 마찬가지로 앞에 역슬래시 \를 붙여 이스케이프 해주면 된다
\ ^ $ . | [ ] ( ) * + ? { }

^[0-9]*$: 숫자
^[a-zA-Z]*$: 영문자. 패턴변경자를 써서 /^[a-z]*$/i 같이 쓸 수 있다.
^[a-zA-Z0-9]*$: 영문/숫자'''