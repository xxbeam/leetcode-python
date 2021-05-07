# 641. 设计循环双端队列

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.capacity = k
        self.head = 0
        self.tail = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size > 0:
            self.head = (self.head + 1) % self.capacity
        else:
            self.head = self.tail = 0
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size > 0:
            self.tail = (self.tail - 1 + self.capacity) % self.capacity
        else:
            self.head = self.tail = 0
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False

if __name__ == '__main__':
    circularDeque = MyCircularDeque(2)
    circularDeque.insertFront(7)
    print(circularDeque.deleteLast())
    print(circularDeque.getFront())
    print(circularDeque.insertLast(5))
    print(circularDeque.insertFront(0))
    print(circularDeque.getFront())
    print(circularDeque.getRear())
    print(circularDeque.getFront())
    print(circularDeque.getFront())
    print(circularDeque.getRear())
    print(circularDeque.insertLast(0))

