# 141.环形链表
import listNode


class Solution:
    def hasCycle(self, head: listNode.ListNode) -> bool:
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            head = head.next
            if fast is head:
                return True
        return False
