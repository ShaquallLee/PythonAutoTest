'''
Descripttion: 归并排序
Author: lishaogang
version: 
Date: 2021-11-15 08:35:33
LastEditors: lishaogang
LastEditTime: 2021-11-15 09:23:51
'''

def merge(arr, left, mid, right):
    res = []
    i,j=left, mid
    while i<mid and j<right:
        if arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    if i<mid:
        res+=arr[i:mid]
    if j<right:
        res+=arr[j:right]
    arr[left:right]=res

def sepSort(arr, left, right):
    if left==right or right-left==1:
        return
    
    mid = left + ((right-left)>>1)
    sepSort(arr, left, mid)
    sepSort(arr, mid, right)
    merge(arr, left, mid, right)


if __name__ == "__main__":
    # import sys
    # sys.setrecursionlimit(100000) #例如这里设置为十万 
    arr = [2,3,1,5,10,4,7,2]
    # test(arr)
    sepSort(arr, 0, len(arr))
    print(arr)