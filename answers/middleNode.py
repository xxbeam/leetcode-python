# 876. 链表的中间结点
import listNode


class Solution:
    def middleNode(self, head: listNode.ListNode) -> listNode.ListNode:
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head = head.next
        return head
