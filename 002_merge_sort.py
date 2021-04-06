def merge_sort(arr, beg, end):
    if beg < end:
        mid = part(arr, beg, end)
        merge_sort(arr, beg, mid - 1)
        merge_sort(arr, mid + 1, end)
    return


def merge(l1, l2):
    ret = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ret.append(l1[i])
            i += 1
        else:
            ret.append(l2[j])
            j += 1
    if i < len(l1):
        ret += l1[i:]
    if j < len(l2):
        ret += l2[j:]
    return ret


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
    l3 = [4, 1, 6, 2, 98, 3, 9, 8, 23, 5]
    ret = part(l3, 0, len(l3) - 1)
    print(ret, l3)

    print(merge([1, 3, 5], [2, 4, 15]))
    ret = merge_sort(l3, 0, len(l3) - 1)
    print(ret)
    print(l3)
