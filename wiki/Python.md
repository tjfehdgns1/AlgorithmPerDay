### Basics


***
### Operators


***
### List

* ###### 추가
```python
my_list = [1,3,5,7,9]
my_list.append(11)  # my_list[len(my_list):] = [11]
print(my_list)  # [1,3,5,7,9,11]
```
* ######
* ###### 정렬
```python
# 리스트의 요소를 절댓값을 기준으로 역으로 정렬하는 예제
numbers = [1,-3,5,2,4]
numbers.sort(key = abs, reverse = True)
print(numbers)  # [5, 4, -3, 2, 1]

# 리스트의 요소를 길이를 기준으로 정렬하는 예제
words = ["banana", "apple", "cherry", "mango"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['apple', 'mango', 'cherry', 'banana']

# 리스트의 요소를 절댓값을 기준으로 정렬하는 예제
numbers = [5, -2, 10, -8, 3]
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers)  # [-2, 3, 5, -8, 10]
```

***
### Tuple


***
### Strings


***
### Sets


***
### Dictionary

##### Built-in functions & methods
* ###### .fromkeys()
```python
keys = ['a', 'b', 'c']
initial_value = 0
dic = dict.fromkeys(keys, initial_value)
print(dic) # {'a': 0, 'b': 0, 'c': 0}
```
```python
string = "hello"
dic = dict.fromkeys(string)
print(dic)# {'h': None, 'e': None, 'l': None, 'o': None}
```
***

### Module



##### Math

```python
import math 

# 상수
math.pi  # 원주율
math.e  # 자연상수
math.tau  # 2pi
math.inf  # 양의 무한대
math.nan  # NaN(Not a Number)

# 지수와 로그 함수
print(math.pow(3, 8))  # 3^8
print(math.exp(2))  # e^2
print(math.expm1(2))  # e^2 - 1
print(math.sqrt(64))  # 8.0, 제곱근
print(math.cbrt(512))  # 8.0, 세제곱근
print(math.log(x), math.log(100,10), math.log10(10))  # ln(x), 2.0, 2.0
print(math.log1p(x))  # ln(1+x)

# 수론 및 표현 함수
print(math.ceil(3.14))  # 4, 올림 
print(math.floor(3.78))  # 3, 내림
print(math.fabs(-3.14))  # 3.14, abs() 절대값
print(math.trunc(-3.14))  # -3, 버림 계산 함수 
print(math.copysign(3.14, -3))  # -3.14, 2번째 인자의 부호를 가져와 1번째 부호에 적용
print(math.comb(n, k))  # nCk, 조합
print(math.perm(n, k))  # nPk, 순열
print(math.factorial(3))  # 3!
print(math.fmod(-x, y))  # -x % y, 부호를 포함한 나머지 출력
print(math.remainder(x, y))  # y의 배수 중 x에 가장 근접한 값을 찾고 그 때 x에서 y의 배수를 뺀 값을 반환
print(math.frexp(100))  # (0.78125, 7), 0.78125 * 2^7 = 100
print(math.ldexp(0.78125, 7))  # 100, 0.78125 * 2^7 = 100
print(math.fsum({1,2,3}))  # 6, (+)
print(math.prod({1,2,3,4}))  # 24, (*)
print(math.gcd(6, 8))  # 2, 양의 최대 공약수
print(math.lcm(13,26))  # 26, 양의 최소 공배수
print(math.modf(3.14))  # (0.14000000000000012, 3.0), 정수와 소수 부분으로 분리해 반환, 부동소수점은 10진법 수를 2진법 체계에서 정확히 반영하지 못해 생기는 문제가 있다
print(math.ulp(x))  # float x의 최하위 비트 값을 반환합니다
print(math.nextafter(6, 0))  # 5.9999..., 6->0을 향한 다음의 부동 소수점 반환

# 삼각함수
math.degrees(), math.radians()  # 라디안->도, 도->라디안
math.cos(), math.sin(), math.tan()  # 라디안에 대한 값 계산
math.acos(), math.asin(), math.atan()  # 역함수
math.cosh(), math.sinh(), math.tanh()  # 쌍곡선 함수
math.acosh(), math.asinh(), math.atanh()  # 역쌍곡선함수
print(math.dist((2,1), (2,0)))  # 1.0, 유클리드 거리
print(math.hypot((1,1)))  # 1.414..., 삼각형 빗면의 유클리드 거리

# 특수 함수
math.erf(x)  # 오차 함수
math.erfc(x)  # 여오차 함수
math.gamma(x)  # 감마 함수
math.lgamma(x)  # 감마 함수의 절댓값의 자연로그를 반환
```



##### Re

*정규표현식*

###### 메타 문자(Meta Characters) : 
> . ^ $ * + ? { } [ ] \ | ( )



1. 문자 클래스 : [a-z], [A-Z], [0-9], [a-zA-Z0-9] 등
* `\d` : 숫자와 매치, [0-9]
* `\D` : [^0-9]
* `\s` : whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
* `\S` : [^ \t\n\r\f\v]
* `\w` : 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]
* `\W` : [^a-zA-Z0-9_]

2. Dot(.) : 줄바꿈(\n)을 제외한 모든 문자와 매치됨
`a.b` == `"a + 모든문자 + b"`


3. 반복(*) : 0부터 무한대로 반복

정규식|문자열|Match|설명
--|--|--|--
`ca*t`|ct|Yes|'a'가 0번 반복
`ca*t`|cat|Yes|'a'가 1번 반복
`ca*t`|caaat|Yes|'a'가 3번 반복</n>

4. 반복(+) : 최소 1번 이상 반복될 때 사용한다

정규식|문자열|Match|설명
--|--|--|--
`ca+t`|ct|No|'a'가 0번 반복, 매치 안됨
`ca+t`|cat|Yes|'a'가 1번 반복
`ca+t`|caaat|Yes|'a'가 3번 반복

5. 반복({m,n}, ?) : m부터 n까지, `? == {0, 1}`

정규식|문자열|Match|설명
--|--|--|--
`ca{2}t`|cat|No|'a'가 1번 반복, 매치 안됨
`ca{2}t`|caat|Yes|'a'가 2번 반복
`ca{2,5}t`|cat|No|'a'가 1번 반복, 매치 안됨
`ca{2,5}t`|caaat|Yes|'a'가 3번 반복
`ca?t`|cat|Yes|'a'가 1번 반복
`ca?t`|ct|Yes|'a'가 0번 반복

###### match

```python
import re

p = re.compile('[a-z]+')
m = p.match('python')
print(m)  # <re.Match object; span=(0, 6), match='python'>
m = p.match('3 python')
print(m)  # none
```

###### search

```python
import re 

p = re.compile('[a-z]+')
s = p.search('3 python')
print(s)  # <re.Match object; span=(2, 8), match='python'>, 일치되는 부분을 찾아준다
```

###### findall

```python
import re

p = re.compile('[a-z]+')
f = p.findall("life is too short")
print(f)  # ['life', 'is', 'too', 'short']
```

###### finditer

```python
import re

p = re.compile('[a-z]+')
f = p.finditer("life is too short")
for r in f: print(r)  # <re.Match object; span=(0, 4), match='life'>
                      # <re.Match object; span=(5, 7), match='is'>
                      #<re.Match object; span=(8, 11), match='too'>
                      #<re.Match object; span=(12, 17), match='short'>
```

###### match 객체의 메소드:

method|목적
--|--
group()|매치된 문자열을 리턴
start()|매치된 문자열의 시작 위치를 리턴
end()|매치된 문자열의 끝 위치를 리턴
span()|매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴

```python
import re

p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())  # 'python'
print(m.start())  # 0
print(m.end())  # 6
print(m.span())  # (0, 6)
```

###### 컴파일 옵션:

옵션|설명
--|--
DOTALL, S|만약 \n 문자도 포함하여 매치하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일
IGNORECASE, I|대소문자 구별 없이 매치를 수행할 때 사용하는 옵션
MULTILINE, M|`^`(시작),`$`(끝) 메타 문자를 문자열의 각 줄마다 적용
VERBOSE, X|줄 단위로 #기호를 사용하여 주석문을 작성

```python
import re

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)  # <re.Match object; span=(0, 3), match='a\nb'>


p = re.compile('[a-z]+', re.I)
p.match('python')  # <re.Match object; span=(0, 6), match='python'>
p.match('Python')  # <re.Match object; span=(0, 6), match='Python'>


p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))  # ['python one', 'python two', 'python three']

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

###### 그루핑:

```python
import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)  # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())  # ABCABCABC

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))  # park

p = re.compile(r'(\b\w+)\s+\1')  # 재참조하기
m = p.search('Paris in the the spring').group()
print(m)  # 'the the'

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")  # 이름 붙이기
m = p.search("park 010-1234-1234")
print(m.group("name"))  # park
```

###### 전방 탐색:

```python
import re 

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())  # http:

p = re.compile(".+(?=:)")  # 긍정형
m = p.search("http://google.com")
print(m.group())  # http

p = re.compile(".*[.](?!bat$).*$", re.M)  # 부정형
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)  # ['autoexec.exe', 'autoexec.jpg']
```

###### 문자열 바꾸기:

```python
import re 

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))  # colour socks and colour shoes
```

###### Greedy & Non-Greedy:

```python
import re

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())  # <html><head><title>Title</title>
print(re.match('<.*?>', s).group())  # <html>
```