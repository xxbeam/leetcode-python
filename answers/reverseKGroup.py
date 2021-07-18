# 25. K 个一组翻转链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # head 与 翻转node合并，并且返回尾节点
        def reverseAndCombat(head: ListNode, node: ListNode):
            reverse_node = None
            tail = node
            while node:
                temp = node
                node = node.next
                temp.next = reverse_node
                reverse_node = temp
            head.next = reverse_node
            tail.next = None
            return tail

        res = ListNode(0)
        res_next = res
        while head:
            count = 0
            # 取出下k个节点
            seg_node = ListNode(0)
            next_node = seg_node
            while count < k and head:
                temp = head
                head = head.next
                next_node.next = temp
                next_node = next_node.next
                next_node.next = None
                count += 1

            # 判断是否满足翻转条件
            if count == k:
                res_next = reverseAndCombat(res_next, seg_node.next)
            else:
                res_next.next = seg_node.next
        return res.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    Solution().reverseKGroup(node1, 2)