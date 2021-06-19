# 203. 移除链表元素
import ListNode

class Solution:

    def removeElements(self, head: ListNode.ListNode, val: int) -> ListNode.ListNode:
        node = ListNode.ListNode(0)
        node.next = head
        temp = node
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return node.next
