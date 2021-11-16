'''
Descripttion: 快速排序
Author: lishaogang
version: 
Date: 2021-11-13 14:34:59
LastEditors: lishaogang
LastEditTime: 2021-11-15 12:08:46
'''
import random

def quickSort(arr, left, right):
    '''
    快速排序
    :param arr: 待排序数组
    :param left: 最左边位置
    :param right: 最右边位置
    :return:
    '''
    if left < right:
        v = arr[left]
        i = left
        j = right
        while i != j:
            while i<j and v < arr[j]:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while i < j and v > arr[i]:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = v
        quickSort(arr, left, i-1)
        quickSort(arr, i+1, right)


def partition(arr, left, right):
    '''
    快速排序一次划分过程，可用于求解荷兰国旗问题、
    荷兰国旗问题：
        对于一个数组，将其划分为大于x、等于x、小于x的三部分
    '''
    prel,prer = left, right
    i = left
    x = arr[right]
    while i<=right:
        if arr[i]<x:
            arr[i], arr[left] = arr[left], arr[i]
            left+=1
            i+=1
        elif arr[i]>x:
            arr[i], arr[right] = arr[right], arr[i]
            right-=1
        else:
            i+=1
    return left-1, right


def quickSort2(arr, left, right):
    if right-left<1:
        return
    x = random.randint(left, right)
    arr[x], arr[right] = arr[right], arr[x]
    nl, nr = partition(arr,left, right)
    quickSort2(arr, left, nl)
    quickSort2(arr, nr, right)

if __name__ == '__main__':
    # arr = [random.randint(0, 100) for i in range(10)]
    arr = [75, 80, 1, 56, 1, 58, 4, 46, 22, 9]
    print(arr)
    # quickSort(arr, 0, 19)
    quickSort2(arr,0,len(arr)-1)
    print(arr)