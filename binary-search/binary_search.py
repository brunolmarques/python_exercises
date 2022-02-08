def recursive_find(arr, x, low, high):
    if (high >= low) and (arr) and (x <= arr[-1]):
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recursive_find(arr, x, low, mid - 1)
        else:
            return recursive_find(arr, x, mid + 1, high)

    else:
        raise ValueError("value not in array")


def find(search_list, value):
    return recursive_find(search_list, value, 0, len(search_list))

