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
### 1. O(1)

*constant complexity*

**Example**
- index, len, append, push, pop 같은 함수들
- 해시 테이블의 원소에 접근
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
### 2. O(log n)

*logarithmic complexity*

**Example**
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
### 3. O(n)

*linear complexity*

**Example**

- for문
- insert, reverse, pop(i), sum, max 같은 함수들
- ...

```python
def linear(arr) : # sum
    output = 0
    for i in range(len(arr)) :
        output += arr[i]
    return output

arr = [1,2,3,4,5]
result = linear(arr)
print(f"합은 {result}입니다") # 합은 15입니다
```

***
### 4. O(nlog n)

*linearithmic complexity*

**Example**

- for문, while문 중첩
- 퀵 정렬(quick sort)
- 병합 정렬(merge sort)
- 힙 정렬(heap sort)
- ...

```python
def linearithmic(arr) : # 퀵 정렬(quick sort)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return linearithmic(lesser_arr) + equal_arr + linearithmic(greater_arr)
    
    given = [7,4,5,1,3]
    result = linearithmic(given)
    print(result) # [1,3,4,5,7]
```

```python
def linearithmic(arr) : # 병합 정렬(merge sort)
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = linearithmic(left_half)
    right_half = linearithmic(right_half)
    
    # 병합
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
            
    merged += left_half[i:]
    merged += right_half[j:]
    
    return merged

given = [1,3,6,2,4,5,7,8]
result = linearithmic(given)
print(result) # [1,2,3,4,5,6,7,8]
```

```python
def linearithmic(arr) : # 힙 정렬(heap sort)
    # 최대 힙 구성 함수
    def heapify(arr, n, i):
        largest = i  # 최대값 인덱스
        l = 2 * i + 1  # 왼쪽 자식 노드 인덱스
        r = 2 * i + 2  # 오른쪽 자식 노드 인덱스

        # 왼쪽 자식 노드가 최대값보다 크면 인덱스 변경
        if l < n and arr[i] < arr[l]:
            largest = l

        # 오른쪽 자식 노드가 최대값보다 크면 인덱스 변경
        if r < n and arr[largest] < arr[r]:
            largest = r

        # 최대값이 루트 노드가 아니면 변경
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # 변경된 자식 노드들에 대해 다시 최대 힙 구성
            heapify(arr, n, largest)

    n = len(arr)

    # 최대 힙 구성
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 정렬 수행
    for i in range(n-1, 0, -1):
        # 루트 노드와 맨 마지막 노드를 교환
        arr[i], arr[0] = arr[0], arr[i]

        # 최대 힙 구성
        heapify(arr, i, 0)

    return arr

given = [5, 2, 9, 3, 7, 6, 1, 8, 4]
result = linearithmic(given)
print(result) # [1,2,3,4,5,6,7,8,9]
```

***

### 5. O(n^2)

*quadratic complexity*

**Example**

- 버블 정렬(bubble sort)
- 선택 정렬(selectrion sort)
- 삽입 정렬(insertion sort)
- 이중 for문
- ...

```python
def quadratic() : # 이중 for문
    for i in range(1, 10): # 구구단
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")
```

```python
def quadratic(arr) : # 버블 정렬(bubble sort)
    n = len(arr)
    
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
given = [7,4,5,1,3]    
result = quadratic(given)
print(result) # [1,3,4,5,7]
```

```python
def quadratic(arr) : # 선택 정렬(selectrion sort)
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # swap
    return arr

given = [64, 25, 10, 22, 11]
result = quadratic(given)
print(result) # [10,11,22,25,64]
```

```python
def quadratic(arr) : # 삽입 정렬(insertion sort)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
given = [5,3,8,4,2]
result = quadratic(given)
print(result) # [2,3,4,5,8]
```

***

### 6. O(2^n)

*exponential complexity*

**Example**

- 피보나치 수열(재귀)
- ...

```python
def exponential(n) : # fibonacci(피보나치 수열)
    if n <= 1 :
        return n
    return exponential(n-1) + exponential(n-2)

given = int(input()) # 10
result = exponential(given)
print(result) # 55
```

***

### 7. O(n!)

**Example**

- 순열의 모든 경우의 수
- ...

```python
def permutation(arr): # 모든 순열
    n = len(arr)
    if n == 0:
        return []
    elif n == 1:
        return [arr]
    result = []
    for i in range(n):
        m = arr[i]
        remain_list = arr[:i] + arr[i+1:]
        for p in permutation(remain_list): # 재귀
            result.append([m] + p)
    return result
given = [1,3,4,2,5]
result = permutation(given)
print(result)
```