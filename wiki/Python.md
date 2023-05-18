### Basics


***
### Operators


***
### List


***
### Tuple


***
### Strings


***
### Sets


***
### Dictionary

##### Built-in functions & methods
###### .fromkeys()
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