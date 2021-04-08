def merge_sort(arr, beg, end):

    if beg < end:
        mid = (beg + end) // 2
        merge_sort(arr, beg, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, beg, mid + 1, end)
    return


def merge(arr, start1, start2, end):
    pre = start1 - 1
    i = start1
    j = start2

    while pre < end and i < end and j < end:
        if arr[i] < arr[j]:
            pre += 1
            arr[pre], arr[i] = arr[i], arr[pre]
            i = pre + 1
        else:
            pre += 1
            arr[pre], arr[j] = arr[j], arr[pre]
            i = max(pre + 1, j)
            j += 1
    return


if __name__ == "__main__":

    l3 = [2, 8, 7, 1, 3, 5, 6, 4]
    merge_sort(l3, 0, 7)
    print(l3)
