#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/04/19 11:00:17
@Author  :    Boxt
@Version :    1.0
@Desc    :    CircularQueue
@Desc_zh :    循环队列
'''

# from typing import List

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
        