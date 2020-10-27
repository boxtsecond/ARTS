ARTS = Algorithm + Review + Tip + Share

Algorithm

这周复习常见的队列操作：

设计一个循环队列

```
'''
设计一个循环队列，leetcode 622
使用数组实现
'''
class SequenceCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = 0
        self.count = 0
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.max:
            return False
        self.queue[(self.count + self.head) % self.max] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.queue[self.head] = None
        self.count -= 1
        self.head = (self.head + 1) % self.max
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.count + self.head) % self.max - 1] 

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.max    

class Node:
    def __init__(self, data: int, _next = None):
        self.data: int = data
        self.next: Node = _next

'''
设计一个循环队列，leetcode 622
使用链表实现，但是链表没有办法体现出“循环”的特点
'''
class LinkedCircularQueue:
    def __init__(self, k: int):
        self.head: Node = None
        self.tail: Node = None
        self.count = 0
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.max:
            return False
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.data
        
    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.data
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.max
```

下周复习常见的队列操作

设计一个双端循环队列
代码已经上传到 GitHub，感兴趣的可以看看

https://github.com/boxtsecond/ARTS
​

Review

薄Six：X-Y PROBLEM[https://zhuanlan.zhihu.com/p/130335668]
​

Tip

循环队列的 Tips

双指针法，两个指针分别指向头指针 head 和尾指针 tail
队空条件：head == tail
队满条件：( tail + 1 ) % limit == head
出队操作：head = ( head + 1 ) % limit
入队操作：tail = ( tail + 1 ) % limit
头指针 head + 队列长度 count
队空条件：count == 0
队满条件：count == limit
出队操作：head = ( head + 1 ) % limit
入队操作：tail = ( head + count ) % limit
Share

薄Six：Kubernetes 架构一览···[https://zhuanlan.zhihu.com/p/133667973]
​
