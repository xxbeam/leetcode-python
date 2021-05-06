# 146. LRU 缓存机制

class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.pre = None

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.lru_map = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.lru_map:
            node = self.lru_map.get(key)
            # 前后节点更新
            self.pop(node)
            # 将节点移至最前面
            self.push_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 判断是否已经在链表中
        if key in self.lru_map:
            node = self.lru_map.get(key)
            # 更新value值
            node.value = value
            # 前后节点更新
            self.pop(node)
        else:
            node = self.Node(key, value)
            if self.size + 1 > self.capacity:
                self.remove_tail()
            else:
                self.size += 1
        # 将节点移至最前面
        self.push_head(node)
        self.lru_map[key] = node

    def push_head(self, node):
        head_node = self.head.next
        head_node.pre = node
        node.next = head_node
        node.pre = self.head
        self.head.next = node

    def remove_tail(self):
        remove_node = self.tail.pre
        pre_node = remove_node.pre
        self.tail.pre = pre_node
        pre_node.next = self.tail
        self.lru_map.pop(remove_node.key)

    def pop(self, node):
        pre_node = node.pre
        next_node = node.next
        next_node.pre = pre_node
        pre_node.next = next_node



if __name__ == '__main__':
    cache = LRUCache(3);
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    print(cache.get(4))
    print(cache.get(3))
    print(cache.get(2))
    print(cache.get(1))
    cache.put(5, 5)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.get(5))





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)