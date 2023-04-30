![](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/07/Big-O-Complexity-Chart.png?resize=1080%2C723&ssl=1)

|Time/n|1|2|3|4|8|16|32|64|1000|
|--|--|--|--|--|--|--|--|--|--|
|1|1|1|1|1|1|1|1|1|1|
|log n|0|1|1.58|2|3|4|5|6|9.97| 
|n|1|2|3|4|8|16|32|64|1000| 
|nlog n|0|2|4.75|8|24|64|160|384|9966| 
|n^2|1|4|8|16|64|256|1024|4096|10^6| 
|2^n|2|4|8|16|256|65536|4294967296|1.844x10^19|1.07x10^301| 
|n!|1|2|6|24|40320|20922789888000|2.63x10^35|1.27x10^89|4.02x10^2567| 

***
### O(1) :

*constant complexity*

##### Example
- index, len, append, pop 같은 함수들
- ...

```python
def constant(arr, index) :
    return arr[index]

arr = [1,2,3,4,5]
index = 1
result = constant(arr, index)
print(result) # 2
```

***
### O(log n) :

*logarithmic complexity*

##### Example
- while문
- 이진 탐색(binary search)
- ...


```python
def logarithmic(n) : # while
    i = 1
    while i < n :
        i *= 2
    return i 
n = 10
result = logarithmic(n)
print(result) # 16
```

```python
def logarithmic(arr, val) : # binary_search
    first, last = 0, len(arr) - 1
    while first <= last :
        mid = (first + last) // 2
        if arr[mid] == val :
            return mid
        elif arr[mid] > val : # 가운데 지점보다 작으면 뒤쪽 반을 자름
            last = mid - 1
        else :
            first = mid + 1
    return -1
arr = [1,3,5,7,9] # 정렬된 자료
find = 7
result = logarithmic(arr, find)
print(f'{result}번째 입니다') # 3번쨰 입니다
```

```python
def logarithmic(target, start, end, data): # recursion(재귀)
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return logarithmic(target, start, end, data)

arr = [1,3,5,7,9]
target = 7
result = logarithmic(target,0,4,arr)
print(f"{result}번쨰 입니다") # 3번째 입니다
```

***
### O(n) :

*linear complexity*

##### Example

- for문
- insert, reverse, pop(i), sum 같은 함수들
- ...

```python
def linear(arr) :
    output = 0
    for i in range(len(arr)) :
        output += arr[i]
    return output

arr = [1,2,3,4,5]
result = linear(arr)
print(f"합은 {result}입니다") # 합은 15입니다
```

