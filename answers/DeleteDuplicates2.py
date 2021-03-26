# 83. 删除排序链表中的重复元素
import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode.ListNode) -> ListNode.ListNode:
        if not head or not head.next:
            return head
        first = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return first
