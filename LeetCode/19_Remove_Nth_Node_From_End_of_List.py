# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        first=second=dummy
        for i in range(n+1):
            first=first.next
        while first:
            second=second.next
            first=first.next
        second.next=second.next.next
        return dummy.next



if __name__ in '__main__':
    obj = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    result = obj.removeNthFromEnd(head, n)
    print(obj.linkedlist_to_list(result))