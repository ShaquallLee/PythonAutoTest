'''
Descripttion: 堆排序
Author: lishaogang
version: 
Date: 2021-11-16 08:38:18
LastEditors: lishaogang
LastEditTime: 2021-11-16 09:21:03
'''

def heapInsert1(heap, heap_size, x):
    heap.insert(heap_size, x)
    i = heap_size
    pos = (i-1)//2
    while x>heap[pos]:
        heap[i], heap[pos] = heap[pos], heap[i]
        i = pos
        pos = (i-1)//2

def heapInsert(heap, i):
    pos = (i-1)//2
    while i>0 and heap[i]>heap[pos]:
        heap[i], heap[pos] = heap[pos], heap[i]
        i = pos
        pos = (i-1)//2

def heapify(heap, heap_size):
    i=0
    left = i*2+1
    while left<heap_size:
        max_pos = left if heap[left]>heap[left+1] else left+1 if left+1<heap_size else left
        if heap[max_pos]>heap[i]:
            heap[max_pos], heap[i] = heap[i], heap[max_pos]
            i = max_pos
            left = i*2+1
        else:
            break

def heapSort(arr):
    if arr is None or len(arr)<2:
        return arr

    heap_size = len(arr)
    for i in range(1, heap_size):
        heapInsert(arr, i)
    
    for i in range(heap_size-1):
        arr[heap_size-1], arr[0] = arr[0], arr[heap_size-1]
        heap_size-=1
        heapify(arr, heap_size)


if __name__ == '__main__':
    arr = [3,1,5,2,7,4,2,10,8]
    heapSort(arr)
    print(arr)
    # heapSort()