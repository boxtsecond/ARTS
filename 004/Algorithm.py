#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/04/12 20:31:51
@Author  :    Boxt
@Version :    1.0
@Desc    :    common stack operations
@Desc_zh :    常见的栈操作
'''

'''
顺序栈，使用数组实现
'''
class SequenceStack:
    def __init__(self, n: int):
        if n <= 0:
            raise "栈的大小不能小于1"

        self.stackArr = [-1] * n  # 栈
        self.length = n     # 栈的规定大小
        self.top = -1       # 栈顶指针

    # 入栈操作
    def push(self, data) -> bool:
        if self.top == self.length - 1:
            return False

        self.top += 1
        self.stackArr[self.top] = data
        return True
    
    # 出栈操作
    def pop(self) -> int:
        if self.top < 0:
            return None
        data = self.stackArr[self.top]
        self.top -= 1
        return data
    
    def isEmpty(self) -> bool:
        if self.top < 0:
            return True
        else: 
            return False
    
    def getTop(self) -> int:
        if self.top < 0:
            return None
        return self.stackArr[self.top]
    
    def getDataStr(self) -> str:
        dataStr = ''
        index = self.top + 1
        while index:
            index -= 1
            dataStr += str(self.stackArr[index])
            
        return dataStr

'''
链式栈，使用链表实现
'''
class Node:
    def __init__(self, data: int, _next = None):
        self.data: int = data
        self.next: Node = _next

class LinkedStack:
    def __init__(self, n: int):
        if n <= 0:
            raise "栈的大小不能小于1"
        self.length = n     # 栈的规定大小
        self.count = 0      # 栈的实际长度
        self.top = None     # 栈顶指针
    
    def push(self, data) -> bool:
        if self.count == self.length:
            return False

        node = Node(data, self.top)
        self.top = node
        self.count += 1
        return True

    def pop(self) -> int:
        if self.count == 0:
            return None
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
    
    def getTop(self) -> int:
        if self.count == 0:
            return None
        return self.top.data
    
    def getDataStr(self) -> str:
        dataStr = ''
        node = self.top
        while node:
            dataStr += str(node.data) + ''
            node = node.next

        return dataStr

    def printStr(self) -> str:
        printStr = ''
        node = self.top
        while node:
            printStr += str(node.data) + ' -> '
            node = node.next

        printStr += 'End'
        return printStr

'''
检验括号匹配
比较含退格的数字
'''
class StackSolutions:

    '''
    检验括号的匹配，leetcode 20
    '''
    def isValid(self, s: str) -> bool:
        # stack = SequenceStack(1000)
        stack = LinkedStack(1000)
        for x in s:
            if x in '({[':
                stack.push(x)
            else:
                y = stack.pop()
                if not y or (x == ')' and y != '(') or (x == '}' and y != '{') or (x == ']' and y != '['):
                    return False
        return stack.isEmpty()       

    '''
    比较含退格的数字，leetcode 844
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.getBackspaceStr(S)
        t = self.getBackspaceStr(T)
        return s == t

    def getBackspaceStr(self, s: str) -> str:
        # stack = SequenceStack(1000)
        stack = LinkedStack(1000)
        for i in s:
            if i == '#':
                stack.pop()
            else:
                stack.push(i)
        return stack.getDataStr()
        

