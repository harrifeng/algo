class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def genListFromArr(nums):
    dummy = ListNode(-1)
    head = dummy

    for num in nums:
        head.next = ListNode(num)
        head = head.next
    return dummy.next


def printList(head):
    while head is not None:
        print(head.val)
        head = head.next


def reversedList(head):
    if head is None or head.next is None:
        return head
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    l1 = genListFromArr([1, 2, 3, 4, 5])
    printList(reversedList(l1))


if __name__ == '__main__':
    main()
