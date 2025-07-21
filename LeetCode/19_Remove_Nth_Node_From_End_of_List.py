# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def linkedlist_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        print(fast)

        # Move fast to the end, maintaining the gap
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the desired node
        slow.next = slow.next.next

        return dummy.next




if __name__ in '__main__':
    obj = Solution()
    head = obj.list_to_linkedlist([1, 2, 3, 4, 5])
    n = 2
    result = obj.removeNthFromEnd(head, n)
    print(obj.linkedlist_to_list(result))