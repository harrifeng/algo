def quick_sort(arr, beg, end):
    if beg < end:
        mid = part(arr, beg, end)
        quick_sort(arr, beg, mid - 1)
        quick_sort(arr, mid + 1, end)
    return


def part(arr, beg, end):
    target = arr[end]
    pre = beg - 1
    i = beg
    while i < end:
        if arr[i] < target:
            pre += 1
            arr[pre], arr[i] = arr[i], arr[pre]
        i += 1
    pre += 1
    arr[pre], arr[end] = arr[end], arr[pre]
    return pre


if __name__ == "__main__":
    l3 = [2, 8, 7, 1, 3, 5, 6, 4]
    ret = part(l3, 0, len(l3) - 1)
    print(ret, l3)

    quick_sort(l3, 0, len(l3) - 1)
    print(l3)
