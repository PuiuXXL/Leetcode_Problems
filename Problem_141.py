# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        return False


list_node1 = ListNode(3)
list_node2 = ListNode(2)
list_node3 = ListNode(0)
list_node4 = ListNode(-4)

list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
# list_node4.next = list_node2

solution = Solution()
print(solution.hasCycle(list_node1))
