# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print(head)



if __name__ in '__main__':
    obj=Solution()
    l=ListNode()
    o=obj.removeNthFromEnd([1,2,3,4,5],2)
    print(o)