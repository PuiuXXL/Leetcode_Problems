# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return []
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

solution = Solution()
list_node1 = ListNode(1)
list_node2 = ListNode(2)
list_node3 = ListNode(3)
list_node4 = ListNode(4)
list_node5 = ListNode(5)

list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
list_node4.next = list_node5

new_list_node = solution.reverseList(list_node1)

current = new_list_node
while current is not None:
    print(current.value)
    current = current.next