#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/04/19 11:00:17
@Author  :    Boxt
@Version :    1.0
@Desc    :    None
@Desc_zh :    双端循环队列
'''

'''
双端循环队列
leetcode 641
'''
class CircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        使用数组实现
        """
        # head 指向起始位置
        self.head   = 0
        # tail 指向已填充位置的后一位
        self.tail   = 0
        # 队列的最大长度，因为 tail 是指向已填充位置的后一位，所以整体的长度需要额外 +1
        self.max    = k + 1
        # 队列
        self.queue  = [None] * self.max

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.head = (self.head + self.max - 1) % self.max
        self.queue[self.head] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.tail] = None
        self.tail = (self.tail + self.max - 1) % self.max
        return True
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        index = (self.tail - 1 + self.max) % self.max
        return self.queue[index]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.tail + 1) % self.max == self.head
            


