"""
    Day15 Stack, Queue
    Version : 1.0
    Created : 2021.12.17
    Updated : 2021.12.17
    Author  : S.M.Lee
"""
import myutils as mu
mu.cprintTitle('stack')
list_stack = []
list_stack.append(1)
list_stack.append(2)
list_stack.append(3)
print(list_stack)
a = list_stack.pop()
print(list_stack, a)
b = list_stack.pop()
c = list_stack.pop()
print(list_stack)

class Stack:
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)
    def pop(self):
        if self.data.isEmpty():
            print("error")
            return
        return self.data.pop()

print('#'*40)
print('queue')
print('#'*40)
# 1. list로 구현
list_queue1 = []
list_queue1.append(1)
list_queue1.append(2)
list_queue1.append(3)
print(list_queue1)
list_queue1.pop(0)
list_queue1.pop(0)
list_queue1.pop(0)

# 2. Queue 클래스로 구현
import queue
import time
print("Queue Class ----------")
q_a = queue.Queue()
time1 = time.time()
for i in range(100000):
    q_a.put(i)
for i in range(100000):
    q_a.get()
time2 = time.time()
print('Queue(Class) :', time2-time1)

q_list = []
time1 = time.time()
for i in range(100000):
    q_list.append(i)
for i in range(100000):
    q_list.pop(0)
time2 = time.time()
print('Queue(List) :', time2-time1)

import myutils as mu
mu.cprintTitle('numpy')

import numpy as np
# 1. 행렬의 생성 1
print('1-1) 1차원 행렬 *****')
list = [1, 2, 3]
array = np.array([1, 2, 3])
print('list :',list)
print('array : ',array)
print(type(list), type(array))

array = np.array(list)

print('1-2) 2차원 행렬 *****')
array = np.array([[1, 2, 3],[4, 5, 6]])
print(array)

print('1-3) 행렬의 차원과 모양 확인 *****')
print('차원 :', array.ndim)
print('모양 :', array.shape)

print('1-4) 행렬의 모양 변경 가능 *****')
array = np.array(range(10))
print(array)
print('길이 :', len(array), ' 값 :', array, ' 차원:', array.ndim)

rarray = array.reshape(2, 5)
print('reshape후 :')
print(rarray, '차원:', rarray.ndim)
print(len(rarray))