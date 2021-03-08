# 206.反转链表
import listNode


class Solution:
    # 迭代
    def reverseList(self, head: listNode.ListNode) -> listNode.ListNode:
        front = None
        while head is not None:
            temp = head.next
            head.next = front
            front = head
            head = temp
        return front

    # 递归
    def reverseList2(self, head: listNode.ListNode) -> listNode.ListNode:
        return self.reverse(head=head, node=None)

    def reverse(self, head: listNode.ListNode, node: listNode.ListNode) -> listNode.ListNode:
        if head:
            temp = head.next
            head.next = node
            return self.reverse(head=temp, node=head)
        return node


if __name__ == '__main__':
    solution = Solution()
    node1 = listNode.ListNode(1)
    node2 = listNode.ListNode(2, node1)
    node3 = listNode.ListNode(3, node2)
    node4 = listNode.ListNode(4, node3)
    node5 = listNode.ListNode(5, node4)

    front = solution.reverseList2(head=node5)
    while front is not None:
        print(front.val)
        print(",")
        front = front.next