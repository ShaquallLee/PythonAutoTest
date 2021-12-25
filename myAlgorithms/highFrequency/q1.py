'''
Descripttion: 两个有序链表连成一个有序链表
Author: lishaogang
version: 
Date: 2021-12-25 08:04:50
LastEditors: lishaogang
LastEditTime: 2021-12-25 08:31:10
'''
import sys
sys.path.append("F:\githubfiles\PythonAutoTest")
from myAlgorithms.utils import Lnode, Mylist

def mergeList(l1, l2):
    head = Lnode()
    node = head
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    
    if l1:
        node.next = l1
    if l2:
        node.next = l2
    return head

if __name__ == "__main__":
    l1 = Mylist(1,3,5,7)
    l2 = Mylist(2,4,6,8)
    print(l1.print(l1.head))
    print(l2.print(l2.head))
    mlist = mergeList(l1.head, l2.head)
    print(Mylist.print(mlist))
