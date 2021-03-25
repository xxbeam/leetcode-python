# 206.反转链表
import ListNode


class Solution:
    # 迭代
    def reverseList(self, head: ListNode.ListNode) -> ListNode.ListNode:
        front = None
        while head is not None:
            temp = head.next
            head.next = front
            front = head
            head = temp
        return front

    # 递归
    def reverseList2(self, head: ListNode.ListNode) -> ListNode.ListNode:
        return self.reverse(head=head, node=None)

    def reverse(self, head: ListNode.ListNode, node: ListNode.ListNode) -> ListNode.ListNode:
        if head:
            temp = head.next
            head.next = node
            return self.reverse(head=temp, node=head)
        return node


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode.ListNode(1)
    node2 = ListNode.ListNode(2, node1)
    node3 = ListNode.ListNode(3, node2)
    node4 = ListNode.ListNode(4, node3)
    node5 = ListNode.ListNode(5, node4)

    front = solution.reverseList2(head=node5)
    while front is not None:
        print(front.val)
        print(",")
        front = front.next