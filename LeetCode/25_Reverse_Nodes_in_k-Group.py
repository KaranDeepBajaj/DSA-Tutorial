class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to get the kth node from current node
        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Get the kth node from group_prev
            kth = get_kth_node(group_prev, k)
            if not kth:
                break  # Not enough nodes to reverse, exit

            group_next = kth.next  # Node after the kth one
            prev = group_next
            curr = group_prev.next

            # Reverse the k nodes
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group with the previous part
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp  # Move group_prev to the end of the reversed group

        return dummy.next
