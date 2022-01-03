'''
Descripttion: 常用类定义
Author: lishaogang
version: 
Date: 2021-12-25 08:05:41
LastEditors: lishaogang
LastEditTime: 2022-01-03 15:07:44
'''


class Lnode():
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class Mylist():
    def __init__(self, *args):
        self.head = Mylist.makeList(*args)

    @staticmethod
    def print(head):
        '''
        返回链表中的值的列表'''
        node = head
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    @staticmethod
    def makeList(*args):
        '''
        生成链表'''
        if args == []:
            return None
        head = Lnode(args[0])
        node = head
        for x in args[1:]:
            newnode = Lnode(x)
            node.next = newnode
            node = newnode
        return head


class Treenode():
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None
