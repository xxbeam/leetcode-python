# 21. 合并两个有序链表
import ListNode


class Solution:

    def mergeTwoLists(self, l1: ListNode.ListNode, l2: ListNode.ListNode) -> ListNode.ListNode:
        head = ListNode.ListNode(0)
        node = head
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return head.next
