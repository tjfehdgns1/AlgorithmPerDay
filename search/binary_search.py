def binary_search(arr, key):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            high = mid
        else:
            low = mid + 1
    return False

if __name__ == "__main__":
    a = list(range(10))
    k = 5
    result = binary_search(a,k)
    if result:
        print('gg')
    else:
        print('whut!')