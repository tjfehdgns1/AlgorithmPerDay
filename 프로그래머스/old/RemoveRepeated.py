'''중복된 문자 제거
문제 설명
문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_string ≤ 110
my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
대문자와 소문자를 구분합니다.
공백(" ")도 하나의 문자로 구분합니다.
중복된 문자 중 가장 앞에 있는 문자를 남깁니다.
입출력 예
my_string	        result
"people"	        "peol"
"We are the world"	"We arthwold"'''

def solution(my_string):
    result = ''
    
    for char in my_string:
        if char not in result:
            result += char
            
    return result
###
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
# ex) {'p': none,'e': none,'o': none,'l': none, } 
# 위 방식들은 후에 나오는 중복된 문자들을 제거하는 방식들

###
#만약 중복된 문자중에서 앞에 있는 문자를 지울려면?
def remove_transposition(my_string: str) -> str:
    pass

