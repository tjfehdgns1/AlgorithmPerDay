def array_operations():
    arr = [1, 2, 4, 5, 6, 7, 8, 9]

    arr.append(10)
    arr.insert(2, 3)
    arr.extend([11, 12])

    arr.reverse()
    arr = list(reversed(arr))

    arr.remove(12)
    arr.pop()

    arr[0]
    arr[:6]
    arr[5:]
    arr[:-1]
    arr[::2]
    arr[::-1]

    len(arr)
    min(arr)
    max(arr)
    arr.count(1)
    arr.index(3)
    arr.sort()
    arr.sort(reverse=True)
    sorted(arr, False)
    arr.copy()
    sum(arr)
    enumerate(arr)
    list(map(str, arr))
    filter(lambda x: x % 2 == 0, arr)
    all([True, True, True]) # True and if empty -> true
    any([False, False, True]) # True and if empty -> false
    set(arr)
    
    arr.clear()