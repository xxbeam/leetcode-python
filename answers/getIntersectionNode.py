# 160. 相交链表
import ListNode

class Solution:

    """
        如果不想交，则两个节点走完headA和headB后必然全部为None
    """
    def getIntersectionNode(self, headA: ListNode.ListNode, headB: ListNode.ListNode) -> ListNode.ListNode:
        node1 = headA
        node2 = headB
        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = headB
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        return node1
