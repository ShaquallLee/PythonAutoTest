'''
Descripttion: 二叉树
Author: lishaogang
version: 
Date: 2021-12-31 14:19:08
LastEditors: lishaogang
LastEditTime: 2021-12-31 14:29:20
'''

def get_max_l(tree):
    if tree is None:
        return 0,0
    # if not tree.left and not tree.right:
    #     return 1
    
    left_l, left_res = get_max_l(tree.left)
    right_l, right_res = get_max_l(tree.right)
    
    res = max([left_l+right_l, left_res, right_res])
    l = max(left_l, right_l)
    return l+1, res