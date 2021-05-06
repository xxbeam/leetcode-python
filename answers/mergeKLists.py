# 23. 合并K个升序链表
import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode.ListNode]) -> ListNode.ListNode:
        def mergeTwoNode(a, b):
            head = ListNode.ListNode(0)
            node = head
            while a and b:
                if a.val < b.val:
                    node.next = a
                    node = a
                    a = a.next
                else:
                    node.next = b
                    node = b
                    b = b.next
            if a is None:
                node.next = b
            if b is None:
                node.next = a
            return head.next
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]
        n = len(lists)//2
        a = self.mergeKLists(lists[:n])
        b = self.mergeKLists(lists[n:])
        return mergeTwoNode(a, b)



if __name__ == '__main__':
    n1 = ListNode.ListNode(1)
    n2 = ListNode.ListNode(4)
    n3 = ListNode.ListNode(5)
    n1.next = n2
    n2.next = n3

    nn1 = ListNode.ListNode(1)
    nn2 = ListNode.ListNode(3)
    nn3 = ListNode.ListNode(4)
    nn1.next = nn2
    nn2.next = nn3

    nnn1 = ListNode.ListNode(2)
    nnn2 = ListNode.ListNode(6)
    nnn1.next = nnn2
    arr = [n1, nn1, nnn1]
    print(Solution().mergeKLists(arr))