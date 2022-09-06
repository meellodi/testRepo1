from math import floor
from tkinter.messagebox import NO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    head1 = l1
    head2 = l2
    carry = 0
    head = None
    while head1 != None or head2 != None:
        val1 = head1.val if head1 != None else 0
        val2 = head2.val if head2 != None else 0
        res = (val1+val2+carry) % 10
        carry = floor((val1+val2+carry) / 10)
        print(val1, val2, res, carry)
        if head == None:
            head = ListNode(res)
            tail = head
        else:
            tail.next = ListNode(res)
            tail = tail.next
        head1 = head1.next if head1 != None else None
        head2 = head2.next if head2 != None else None
    if carry > 0:
        tail.val = carry
    return head


l1 = ListNode(1)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)

k1 = ListNode(1)
k2 = ListNode(9, k1)
k3 = ListNode(4, k2)

res = addTwoNumbers(l3, k3)
while res != None:
    print(res.val)
    res = res.next
