def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array

    mid = len(array) // 2

    low = merge_sort(array[:mid])
    high = merge_sort(array[mid:])

    merged_array = []
    l, h = 0, 0

    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merged_array.append(low[l])
            l += 1
        else:
            merged_array.append(high[h])
            h += 1

    merged_array += low[l:]
    merged_array += high[h:]

    return merged_array


arr = [6, 5, 1, 4, 3, 2, 8, 7]
print(merge_sort(arr))
