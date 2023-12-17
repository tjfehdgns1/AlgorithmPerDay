array = [3,4,2,1,5,8,7,6,0,9]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(array, 0, len(array) - 1)

print(array)
    
# --- #

def py_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return py_quick_sort(left) + [pivot] + py_quick_sort(right)

print(py_quick_sort(array))



def quick_sort1(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort1(left) + middle + quick_sort1(right)

# 테스트
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort1(arr)
print(sorted_arr)
