#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/03/20 15:30:44
@Author  :    Boxt
@Version :    1.0
@Desc    :    common linked list operations 
@Desc_zh :    常见的链表操作
'''

'''
求链表的中间结点
链表中环的检测
单链表反转
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
    求链表的中间结点，leetcode 876
    1. 输出到数组，获取[length/2]的结点
       时间复杂度 O(n)
       空间复杂度 O(n)
    2. 快慢指针，快指针步长为2，慢指针步长为1，当快指针到达终点，慢指针指向中间结点
       时间复杂度 O(n)
       空间复杂度 O(1)
    '''
    def findMiddleNode_1(self, head: ListNode) -> ListNode:
        A = []
        currentNode = head.next
        # 链表只有头结点
        if not currentNode:
            return head
        while currentNode:
            A.append(currentNode)
            currentNode = currentNode.next
        return A[len(A) / 2]

    def findMiddleNode_2(self, head: ListNode) -> ListNode:
        # 链表只有头结点
        if not head or not head.next:
            return head
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    '''
    链表中环的检测，leetcode 142
    1. 遍历链表，并记录链表的结点，若有重复，则有环，返回重复的结点
       时间复杂度 O(n)
       空间复杂度 O(n)
    2. 快慢指针相遇法，快指针步长为2，慢指针步长为1，
       假设环的长度远大于入环前的长度，即快慢指针相遇在环的第一圈中
       a. 假设入环前的长度为 n，当慢指针到达入环点时，快指针走完入环前的长度并在环内走了 n
       b. 假设快指针在环内剩余的长度为 r，即 r + n = 环长
       c. 当慢指针开始入环并在环内走过 r 的长度，此时快指针走过 2r 的长度，即快指针走过之前在环内剩余的长度 r，并继续在入环点后走了 r
       d. 快慢指针相遇在距离入环点 r 的位置，此时相遇点距离入环点为 n，正好为入环点前的长度
       e. 此时两个慢指针分别从头结点，相遇点出发，再次相遇时则为入环点
       如果快慢指针相遇在绕环的多圈后，可以想成多个小环铺展开成一个大环，则仍旧是上述环的长度远大于入环前长度的情况
       时间复杂度 O(n)
       空间复杂度 O(1)
    '''
    def detectCycle_1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nodes = set()
        currentNode = head
        while currentNode:
            if currentNode in nodes:
                return currentNode
            else:
                currentNode = currentNode.next
        return None
    
    def detectCycle_2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        meetNode = self.__getMeetNode(head)
        if not meetNode:
            return None
        currentNode = head
        while currentNode != meetNode:
            currentNode = currentNode.next
            meetNode = meetNode.next
        return currentNode
        
    def __getMeetNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow
        return None
    '''
    单链表反转  leetcode 206
    1. 重新一个生成链表
       时间复杂度 O(n)
       空间复杂度 O(n)
    2. 递归解法，这个不太好理解，还是去 leetcode 看动画演示便于理解
       时间复杂度 O(n)
       空间复杂度 O(n)
    3. 双指针，一个指向当前结点，另一个指向前一个结点
       时间复杂度 O(n)
       空间复杂度 O(1)
    '''
    def reverseLinkedList_1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reverseHead = ListNode(head.data)
        currentNode = head.next
        while currentNode:
            node = ListNode(currentNode.data, reverseHead)
            reverseHead = node
            currentNode = currentNode.next
        return reverseHead

    def reverseLinkedList_2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  
        node = self.reverseLinkedList_2(head.next)
        head.next.next = head
        head.next = None
        return node       

    def reverseLinkedList_3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        prevNode = head
        currentNode = head.next
        while currentNode:
            tmp = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = tmp
        head.next = None
        head = prevNode
        return head

    '''
    得到链表中 data 的字符串
    '''    
    def printLinkedList(self, node: ListNode) -> str:
        printStr = ''
        while(node):
            printStr += str(node.data) + ' -> '
            node = node.next

        printStr += 'End'
        return printStr
