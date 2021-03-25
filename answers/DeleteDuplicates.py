# 82. 删除排序链表中的重复元素 II
import ListNode

class Solution:

    def deleteDuplicates(self, head: ListNode.ListNode) -> ListNode.ListNode:
        # 如果列表为空或者只有一个元素，直接返回
        if not head or head.next is None:
            return head
        first = head
        has_dup = False
        head = head.next
        # 排除头部重复数据
        while head:
            if first.val == head.val:
                if not has_dup:
                    has_dup = True
                head = head.next
                continue
            else:
                if has_dup:
                    first = head
                    head = head.next
                    has_dup = False
                else:
                    break
        # 从头到尾都是重复的
        if has_dup:
            return None
        # 如果第二个节点或者第三个节点为空 则返回
        if not head or not head.next:
            return first
        node = first
        sec = head
        head = head.next
        while head:
            if sec.val == head.val:
                if not has_dup:
                    has_dup = True
                head = head.next
            else:
                if has_dup:
                    first.next = head
                    has_dup = False
                else:
                    first = sec
                sec = head
                head = head.next
        if has_dup:
            first.next = None
        return node


if __name__ == '__main__':

    node1 = ListNode.ListNode(1)
    node2 = ListNode.ListNode(2)
    node3 = ListNode.ListNode(3)
    node4 = ListNode.ListNode(3)
    node5 = ListNode.ListNode(4)
    node6 = ListNode.ListNode(4)
    node7 = ListNode.ListNode(5)
    node1.next = node2
    node2.next = node3




