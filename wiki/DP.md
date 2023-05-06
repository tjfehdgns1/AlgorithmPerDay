### 동적 계획법(DP)

*Dynamic Programming*

***

동적 계획법은 이름과 달리 동적이지 않고 어떠한 값을 기억하면 문제를 푸는 것이 본질이라고 할 수 있다.

**조건 :**

* 최적부분구조(Optimal Substructure)
* 중복되는 부분 문제(Overlapping Subproblems)
***

* 메모이제이션(Memoization) : cache에 값을 기록

```python
def fibo(x) : # Top-Down
    # 종료 조건
    if x == 1 or x == 2 :
        return 1
    # 기억
    if d[x] != 0 :
        return d[x]
    # 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

d = [0] * 100
x = 99
result = fibo(x) # 218922995834555169026
```

***

* 타뷸레이션(Tabulation) : 리스트에 값을 기록

```python
def fibo(x) : # Bottom-Up
    d = [0] * 99
    d[1], d[2] = 1, 1
    for i in range(3,x+1) :
        d[i] = d[i-1] +[i-2]

    return d[x]
x = 99
result = fibo(x) # 218922995834555169026
```