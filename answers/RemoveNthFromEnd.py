# 19. 删除链表的倒数第 N 个结点
import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode.ListNode, n: int) -> ListNode.ListNode:
        fast = head
        slow = head
        while n > 0:
            fast = fast.next
            n -= 1
            # 因为n小于等于链表长度，如果fast为空，则表示删除的是链表的第一位
            if not fast:
                return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
