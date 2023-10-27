from bisect import bisect_left, bisect_right

def countnum(l, r, arr) :
    l = bisect_left(arr, l)
    r = bisect_right(arr, r)
    return  r - l

x = 2
given = [1,1,2,2,2,2,3]

count = countnum(x,x,given)

if count == 0 :
    print(-1)
else :
    print(count) # 4

