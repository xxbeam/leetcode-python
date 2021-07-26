# 138. 复制带随机指针的链表

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        res = Node(0)
        temp = res
        while head:
            old_node = head
            head = head.next

            copy_node = Node(x=old_node.val, random=old_node.random)
            # 将old_node的next指针指向copy_node
            old_node.next = copy_node
            temp.next = copy_node
            temp = copy_node
        temp = res.next
        while temp:
            if temp.random:
                # 由于在上步中将old的next指向了copy，所以如果存在random的node，直接取node.next则为copy后的数据
                temp.random = temp.random.next
            temp = temp.next
        return res.next

