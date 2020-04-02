#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :    Algorithm.py
@Time    :    2020/03/31 14:09:45
@Author  :    Boxt
@Version :    1.0
@Desc    :    common stack operations
@Desc_zh :    常见的栈操作
'''

'''
数制转换
表达式求值
'''
from typing import List

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
        while(node):
            dataStr += str(node.data) + ''
            node = node.next

        return dataStr

    def printStr(self) -> str:
        printStr = ''
        node = self.top
        while(node):
            printStr += str(node.data) + ' -> '
            node = node.next

        printStr += 'End'
        return printStr

'''
数制转换
表达式求值
'''
class StackSolutions:

    '''
    十进制与其他进制间的转换
    @param number  十进制数字
    @param number  转换的进制
    '''
    def decimalBinaryConverter(self, number: int, binarySystem: int) -> str:
        stack = SequenceStack(100)
        # stack = LinkedStack(100)
        if number < binarySystem:
            return self.convertNumber(number)
        while number > 0:
            stack.push(self.convertNumber(number % binarySystem))
            number = int(number / binarySystem)
        return stack.getDataStr()

    '''
    转换进制中的特殊字符
    字符A 的 ascii 码为65，对应十进制的 10，所以用十进制数字 + 55 就是特殊字符的 ascii 码
    '''
    def convertNumber(self, number: int) -> str:
        if number < 10:
            return str(number)
        else:
            return chr(number + 55) 

    '''
    表达式求值，leetcode 150
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = SequenceStack(50)
        stack = LinkedStack(50)
        for x in tokens:
            if x not in '+-*/':
                stack.push(int(x))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(self.getResult(num1, num2, x))
        return stack.pop()

    '''
    升级版表达式求值
    输入的不是数组，而是直接的表达式字符串，不考虑表达式不成立、空格、存在负数的情况
    题目分析：
    1. 运算的优先级：括号内的子表达式 > 乘除 > 加减，在括号里的子表达式遵循的也是 乘除 > 加减，所以在实际的实现中，其实是 乘除 > 括号内部 > 加减
    2. 数字字符串需要转换成数字
    3. 做减法时，改为加一个负数
    代码实现：
    1. 使用两个栈，一个用来存放数字（数字栈），一个用来存放运算符和括号（运算栈）
    2. 字符为左括号时，不进行任何操作，直接推入运算栈中
    3. 字符为右括号时，计算出与它对应的左括号（运算栈持续出栈操作后遇到的第一个左括号）组成的表达式的值，推入数字栈中
    4. 字符为运算符时，如果是乘除的话，计算表达式，如果是减号的话，改为加一个负数
    '''
    # 10*(6/((9+3)*11))+17+5-6  = 16
    # ((2+1)*3)                 = 9
    # 4+(13/5)                  = 6
    # 2*3*6-4                   = 32
    # 4+2*3*6-4                 = 36
    # (12+33*8)*10              = 2796
    # 4+6/2/3                   = 5
    # 4+2*3*6-4+(12+33*8)*10    = 4076
    # 3+4-5+8                   = 10
    # 1+2-1/1/1/1/1+100         = 102
    # 1+1-1-1-1-1               = -2
    # 10/(2+3)                  = 5
    def evalRPNHard(self, exp: str) -> str:
        # numStack = SequenceStack(50)
        # expStack = SequenceStack(50)
        numStack = LinkedStack(50)      # 存放数字
        expStack = LinkedStack(50)      # 存放运算符和括号
        priority = {                    # 运算符的优先级
            '+': 1, '-': 1,         
            '*': 2, '/': 2,
        }
        numStr = ''
        for x in exp:
            if x == '(':
                expStack.push(x)
            elif x == ')':
                numStr = self.pushNumByStr(numStack, numStr)
                numStack.push(self.getInnerResult(priority, numStack, expStack))
            elif x not in '+-*/':
                numStr += x
            else:
                numStr = self.pushNumByStr(numStack, numStr)
                higherResult = self.getHigherPriorityResult(priority, numStack, expStack, x)
                if higherResult:
                    numStack.push(higherResult)
                if x == '-':
                    numStr = self.pushNumByStr(numStack, numStr)
                    numStr += x
                    x = '+'
                expStack.push(x)
        self.pushNumByStr(numStack, numStr)
        return self.getSamePriorityResult(numStack, expStack)
    
    '''
    数字字符串转换为数字，并推入数字栈中
    '''
    def pushNumByStr(self, numStack: LinkedStack, numStr: str):
        if numStr:
            numStack.push(int(numStr))
            numStr = ''
        return numStr

    '''
    计算括号内子表达式的值
    '''
    def getInnerResult(self, priority, numStack: LinkedStack, expStack: LinkedStack) -> int:
        exp = expStack.pop()
        result = numStack.pop()
        while exp and exp != '(':
            num = numStack.pop()
            result = self.getResult(num, result, exp)
            exp = expStack.pop()
        return result

    '''
    计算高优先级表达式的值
    '''
    def getHigherPriorityResult(self, priority, numStack: LinkedStack, expStack: LinkedStack, x: str) -> int:
        e = expStack.getTop()
        result = None
        if not e:
            return result
        
        result = numStack.pop()
        while priority.get(e, 0) > 1:
            num = numStack.pop()
            result = self.getResult(num, result, e)
            expStack.pop()
            e = expStack.getTop()
        return result

    '''
    计算相同优先级表达式的值
    '''
    def getSamePriorityResult(self, numStack: LinkedStack, expStack: LinkedStack) -> int:
        result = numStack.pop()
        while not numStack.isEmpty():
            n = numStack.pop()
            e = expStack.pop()
            result = self.getResult(n, result, e)
        return result
    
    '''
    计算操作
    '''
    def getResult(self, num1: int, num2: int, exp: str) -> int:
        if exp == '-':
            return num1 - num2
        elif exp == '*':
            return num1 * num2
        elif exp == '/':
            return int(num1 / num2)
        else:
            return num1 + num2
