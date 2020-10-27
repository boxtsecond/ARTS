
ARTS = Algorithm + Review + Tip + Share

Algorithm

这周复习以下常见的链表操作：

两个有序的链表合并
删除链表的倒数第 n个结
下周复习常见的栈的应用：

数制转换
表达式求值

```
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

    '''
    删除链表的倒数第 n 个结点 leetcode 19
    1. 暴力解法，遍历两次
    第一次遍历找到倒数第 n 个结点，第二次遍历匹配到找到的结点，然后删除
    时间复杂度O (n)
    空间复杂度O (1)
    *这个就不写了*
    2. 双指针解法
    第一个指针先行 n 个结点，然后第二个指针从头结点出发，两个指针同时前行，当第一个指针到达终点时，第二个指针指向倒数第 n 个结点
    Tip：使用哨兵结点来简化判断逻辑
    时间复杂度O (n)
    空间复杂度O (1)
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prevNode = ListNode(-1)
        prevNode.next = head
        fast = slow = prevNode
        while n != 0 and fast:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return prevNode.next
```

代码已经上传到 GitHub，感兴趣的可以看看

https://github.com/boxtsecond/ARTS
​
这两周一起复习了单向链表最基础的操作，现在对这些思路和方法做一下总结

最常见的方法：双指针法
单向链表使用两个指针分别指向当前结点和前一个结点。
利用两个指针不一样的步长，找到结点间的倍数关系。如找到链表的中间结点使用的是两倍步长的快指针，同理可得找到 1/3 处的结点，是使用三倍步长的快指针。
利用两个指针的差值，找到结点间的差值关系。如找到链表的倒数第n个结点。
最常见的小 Tips
利用哨兵结点简化判断逻辑。如两个有序链表的合并，使用哨兵结点来简化判断两个链表的最小值。
当需要对“环”做一些操作时，可以先按照较大的“环”来处理，然后将“大环”想象成是多个“小环”铺展开的情况。
代码实现的注意点
插入结点时，注意操作顺序
删除结点时，主要内存泄漏问题（考虑是否需要手动释放内存空间）
指针的步长大于 1 时，注意判断是否还存在下一个结点
注意边界条件的处理
链表为空
链表只包含一个结点（有时还要特殊考虑只包含两个结点的情况）
头结点和尾结点是否需要特殊处理
Review

https://www.quora.com/What-are-some-of-the-most-basic-things-every-programmer-should-know
​
程序员应该知道的常识有哪些（根据自己的理解筛选了一部分，欢迎大家补充～）

永远都不要使用没测试过的代码。
一定要使用版本控制。
团队中的小伙伴修改自己写的代码很正常，自己写的代码不是完美的，别人写的代码也不总是 shit，对自己的“战友”大方点、宽容点。
不要重复造轮子。
最好最快的代码的是从未执行过的代码，看看能不能提前 return。
不容易理解的代码不好维护，不好维护的代码就是会被后人吐槽并重构的代码（意味着你写的代码没人想要看和用）。
代码不会说话，不会自己解释逻辑，求求你写几句注释吧！！！（来自看遗留代码到想哭的人）
烂代码不会自己消失，现在或将来一定会缠着你。
没有5分钟能解决的事儿，最小的时间单位是半天。
不要直接在代码里写死数字。这个请参见第 7 条。
如果有bug一定会被用户发现的。
Code Review 不是批斗会。
代码的数量不重要，重要的是质量。
自己写的烂代码要及时修正，自己造的孽自己要负责。

Tip

Linux 设置开机默认进入文字模式（Ubuntu 12.04）

修改文件 /etc/default/grub 的 GRUB_CMDLINE_LINUX_DEFAULT 信息，改为 “text”（原来为“quiet splash”）。保存文件并退出后，执行 sudo update-grub 来更新修改的内容。之后重启一下就可以看到设置已经生效了。

GRUB_CMDLINE_LINUX_DEFAULT 只能在普通情况下生效，不会在 recovery mode 下生效，GRUB_CMDLINE_LINUX 会在所有情况下生效。

大概说下这三个单词代表的意思

quiet 不显示 Ubuntu 启动信息
splash 显示启动画面
text 显示启动信息
如果设置后出现什么异常情况，不能正常启动，可以使用 Ctrl + Alt + F1 ~ F6 来切换窗口登陆，登陆后就可以再对设置做一些修改。

Linux 预设提供了六个命令窗口终端机让我们来登录。默认登录的是第一个窗口，也就是tty1，这个六个窗口分别为tty1,tty2 … tty6，按下Ctrl + Alt + F1 ~ F6 可以切换到相应的窗口。如果想要进入图形界面的话，可以在命令行输入 sudo init 5，就会有一个新的图形界面，位置是在第七个窗口，按下 Ctrl + Alt + F7 切换到图形界面。可以利用tty1～tty6考虑同时登陆多个用户。

这个小 Tip 的背景：在公司有一个台式机，里面放着一些文件，有的时候需要查看这些文件的内容（很少的情况），每次等 GUI 的时间有点久，所以就改成开机直接进入文字模式。有类似需求的小伙伴可以试试这个方法。

Share

薄Six：容器镜像的设计与实现[https://zhuanlan.zhihu.com/p/115659428]
