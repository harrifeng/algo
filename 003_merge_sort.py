def merge_sort(arr, beg, end):

    if beg < end:
        mid = (beg + end) // 2
        merge_sort(arr, beg, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, beg, mid + 1, end)
    return


def merge(arr, start1, start2, end):

    l1 = [i for i in arr[start1:start2]]
    l2 = [j for j in arr[start2 : end + 1]]

    print("before-->", l1, l2, arr[start1 : end + 1])

    i = 0
    j = 0
    curr = start1

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            arr[curr] = l1[i]

            i += 1
        else:
            arr[curr] = l2[j]
            j += 1
        curr += 1
    while i < len(l1):
        arr[curr] = l1[i]
        curr += 1
        i += 1
    while j < len(l2):
        arr[curr] = l2[j]
        curr += 1
        j += 1
    print("after--->", l1, l2, arr[start1 : end + 1])
    print("----------------")
    return


if __name__ == "__main__":

    # ll = [1, 3, 5, 2, 4, 6, 8]
    # merge(ll, 0, 3, 6)
    # print(ll)
    l3 = [2, 8, 7, 1, 3, 5, 6, 4]
    print(l3)
    merge_sort(l3, 0, 7)
    print(l3)
