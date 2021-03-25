# 876. 链表的中间结点
import ListNode


class Solution:
    def middleNode(self, head: ListNode.ListNode) -> ListNode.ListNode:
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head = head.next
        return head
