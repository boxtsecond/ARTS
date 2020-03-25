#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/03/25 14:42:33
@Author  :    Boxt
@Version :    1.0
@Desc    :    common linked list operations 
@Desc_zh :    常见的链表操作
'''

'''
两个有序的链表合并
删除链表的倒数第 n 个结点
'''
from typing import List

'''
链表中的结点
'''
class ListNode:
    def __init__(self, data: int, _next = None):
        self.data = data
        self.next = _next

'''
链表
'''
class LinkedList:
    def __init__(self, dataArr: List[int]):
        head = prevNode = None
        for index, nodeData in enumerate(dataArr):
            node = ListNode(nodeData)
            if index == 0:
                head = prevNode = node
            else:
                prevNode.next = node
                prevNode = node
        self.__head = head

    def getHead(self):
        return self.__head
    
class LinkedListSolution:
    '''
    两个有序的链表合并  leetcode 21
    1. 递归方式，利用函数栈新增新的结点
       Tip：在递归调用的过程当中系统为每一层的返回点、局部量等开辟了栈来存储，递归的本质就是栈，因此递归次数过多容易造成栈溢出。
       时间复杂度 O(n+m)
       空间复杂度 O(n+m)
    2. 迭代方式，利用哨兵结点来简化判断最小结点
       时间复杂度 O(n+m)
       空间复杂度 O(1)
    '''
    def merge2SortedLinkedList_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # 在 leetcode 上，需要把 data 字段换成 val 字段
        if l1.data < l2.data:
            l1.next = merge2SortedLinkedList_1(l1.next, l2)
            return l1
        else:
            l2.next = merge2SortedLinkedList_1(l1, l2.next)
            return l2
        

    def merge2SortedLinkedList_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        prevNode = head = ListNode(-1)
        while l1 and l2:
            # 在 leetcode 上，需要把 data 字段换成 val 字段
            if l1.data < l2.data:
                prevNode.next = l1
                l1 = l1.next
            else:
                prevNode.next = l2
                l2 = l2.next
        prevNode.next = l1 if l1 else l2 
        return head.next
                

