def FindFirstCommonNode(self, pHead1, pHead2):
    #思路一：利用两个栈来实现
    # write code here
    stack1 = []
    stack2 = []
    while pHead1:
        stack1.append(pHead1)
        pHead1 = pHead1.next
    while pHead2:
        stack2.append(pHead2)
        pHead2 = pHead2.next
    result = None
    while stack1 and stack2:
        tmp1 = stack1.pop()
        tmp2 = stack2.pop()
        if tmp1 == tmp2:
            result = tmp1
        else:
            break
    return result


def FindFirstCommonNode2(self, pHead1, pHead2):
    length1 = 0
    length2 = 0
    head1 = pHead1
    head2 = pHead2
    while head1:
        length1 += 1
        head1 = head1.next
    while head2:
        length2 += 1
        head2 = head2.next
    sub = abs(length1 - length2)
    for i in range(sub):
        head1 = head1.next if length1 > length2 else head2 = head2.next
    # if length1 >= length2:
    #     for i in range(sub):
    #         pHead1 = pHead1.next
    # elif length2 > length1:
    #     for i in range(sub):
    #         pHead2 = pHead2.next
    while pHead1 != pHead2:
        pHead1 = pHead1.next
        pHead2 = pHead2.next
    return pHead1
