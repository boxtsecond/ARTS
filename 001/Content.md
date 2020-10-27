
ARTS = Algorithm + Review + Tip + Share

Algorithm

这周复习以下常见的链表操作：

求链表的中间结点（ leetcode 876 ）
链表中环的检测（ leetcode 142 ）
单链表反转（ leetcode 206 ）
下周复习其他两个常见的链表操作：

两个有序的链表合并
删除链表的倒数第 n个结点

```
'''
链表中结点
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
    2. 递归解法，这个不太好理解，还是去 leetcode 看动画演示吧
       动画地址：https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
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
    def printLinkedList(node: ListNode) -> str:
    printStr = ''
    while(node):
        printStr += str(node.data) + ' -> '
        node = node.next

    printStr += 'End'
    return printStr
```

代码已经上传到 GitHub，感兴趣的可以看看

https://github.com/boxtsecond/ARTS
​
Review

The Key to Accelerating Your Skills While You Learn to Code
​
blog.thefirehoseproject.com[http://blog.thefirehoseproject.com/posts/learn-to-code-and-be-self-reliant/]

快速提高代码能力的小技巧

入门前准备阶段
在特定领域学习，完成特定的小任务。例如：知道如何用Ruby编写循环或如何使用Ruby on Rails从数据库中提取内容。
2. 入门阶段

学会阅读报错信息。
从解决的报错信息中学习，了解为什么会出现这个错误，以及如何修复。
知道如何准确描述遇到的问题或错误，并自行 Google。
3. “慢增长”阶段

前两个阶段会让自己感受到每天都在快速吸收知识，快速成长。而在这个阶段，会开始意识到需要学习基础知识（数据结构和算法）和底层知识，会感觉比前两个阶段进步的要慢 10 ～ 20 倍，但其实这个阶段是“指数型增长”的阶段，前期积累好，后期增幅巨大。
每天都要超越之前的自己，不断地跳出舒适圈。
不要追逐“潮流”。不要因为最近 Python 火就去学 Python，当完成“慢增长”阶段后，学习一个“新潮流”不会是一件困难的事情。
有意识的积累自己的“代码库”。将自己之前完成过的功能，尽可能的写成通用型，之后可以很快的稍作改动就复用。例如：发送邮件（只需改动发件人、密码等）、对接微信支付宝等（改动密钥等）。
尽可能的阅读文档，而不是教程。
4. 如何能完成全部的阶段

知道这是一条充满荆棘的道路，遇到各种各样的困难是正常的，心态要保持放松。
要“细水长流”的坚持，而不是和“暴风雨”一样的短暂。当然，太“细”了也不行，没有效果，要把握一个可以长期坚持的度。
Tip

Mysql group_concat() 函数的返回值被截断
group_concat() 函数的返回值大小默认为1024字节，多余部分将会被截断。
解决办法，通过设置group_concat() 函数的返回值大小 group_concat_max_len：
在 /etc/my.cnf 中的[mysqld]加上group_concat_max_len = 1024000，需要重启mysql才能生效
全局设置：SET GLOBAL group_concat_max_len=1024000; 或者 每次会话使用 SET SESSION group_concat_max_len=1024000;
Share

https://zhuanlan.zhihu.com/p/92802421[https://zhuanlan.zhihu.com/p/92802421]

分享一篇之前写过的Docker镜像命令的文章