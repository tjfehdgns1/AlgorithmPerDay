def list_operations():
    l = [1, 2, 4, 5, 6, 7, 8, 9]

    l.append(10)
    l.insert(2, 3)
    l.extend([11, 12])

    l.reverse()
    l = list(reversed(l))

    l.remove(12)
    l.pop()

    l[0]
    l[:6]
    l[5:]
    l[:-1]
    l[::2]
    l[::-1]

    len(l)
    min(l)
    max(l)
    l.count(1)
    l.index(3)
    l.sort()
    l.sort(reverse=True)
    sorted(l, False)
    l.copy()
    sum(l)
    enumerate(l)
    list(map(str, l))
    filter(lambda x: x % 2 == 0, l)
    all([True, True, True]) # True and if empty -> true
    any([False, False, True]) # True and if empty -> false
    set(l)
    
    l.clear()