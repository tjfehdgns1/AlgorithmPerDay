def solution(d, budget):
    d.sort()
    count = 0
    for n in d :
        budget -= n
        if budget < 0 :
            budget += n
            count -= 1
        count += 1
    return count

def solution1(d, budget):
    d.sort()
    count = 0
    for n in d :
        budget -= n
        if budget < 0 :
            break
        count += 1
    return count

def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
