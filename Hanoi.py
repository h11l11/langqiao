#汉诺塔问题的解决
# def hanoi(n, a, b, c):
#     if n > 0:
#         hanoi(n - 1, a, c, b)
#         print(str(n) + " moving from " + a + " to " + c)
#         hanoi(n - 1, b, a, c)
#
#
# hanoi(3, 'a', 'b', 'c')
# 二分法查找
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val:
#             right = mid - 1
#         elif li[mid] < val:
#             left = mid + 1
#     else:
#         return None
#
#
# li = [1, 2, 3, 4, 5, 6, 6, 7]
# val = 3
# print(binary_search(li, val))

# 冒泡排序
# def bubble_sort(li):
#     for i in range(len(li) - 1):
#         exchange = False
#         for j in range(len(li) - i - 1):
#             if li[j] > li[j + 1]:
#                 li[j], li[j + 1] = li[j + 1], li[j]
#                 exchange = True
#         if not exchange:
#             return
#
#
# li = [1, 3, 4, 2, 4, 6]
# bubble_sort(li)
# print(li)
# 选择排序算法
# def select_sort(li):
#     for i in range(len(li) - 1):
#         min_loc = i
#         for j in range(i, len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         if min_loc != i:
#             li[i], li[min_loc] = li[min_loc], li[i]
#
#
# li = [1, 2, 34, 5, 2, 9]
# select_sort(li)
# print(li)

# 插入排序算法
# def insert_sort(li):
#     for i in range(1, len(li)):
#     #     for j in range(i):
#     #         if li[i] < li[j]:
#     #             li[i], li[j] = li[j], li[i]
#         temp = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > temp:
#             li[j+1] = li[j]
#             j -= 1
#         li[j+1] = temp
#
#
# li = [1, 2, 4, 6, 3, 9, 5]
# insert_sort(li)
# print(li)

#快速排序
#比冒泡排序要快
# def partition(data, left, right):
#     tmp = data[left]
#     while left < right:
#         while left < right and data[right] >= tmp:
#             right -= 1
#         data[left] = data[right]
#         while left < right and data[left] <= tmp:
#             left += 1
#         data[right] = data[left]
#     data[left] = tmp
#     return left
#
#
# def quick_sort(data, left, right):
#     if left < right:
#         mid = partition(data, left, right)
#         quick_sort(data, left, mid - 1)
#         quick_sort(data, mid + 1, right)


#堆排序
# def sift(li, low, high):
#     i = low
#     j = 2 * i + 1
#     tmp = li[low]
#     while j <= high:
#         if j + 1 <= high and li[j + 1] > li[j]:
#             j = j + 1
#         if li[j] > tmp:
#             li[i] = li[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             li[i] = tmp
#             break
#     else:
#         li[i] = tmp
# def heap_sort(li):
#     n = len(li)
#     for i in range((n - 2)//2, -1, -1):
#         sift(li, i, n - 1)
#     for i in range(n - 1, -1, -1):
#         li[0], li[i] = li[i], li[0]
#         sift(li, 0, i - 1)

#topk问题
#即有n个数，要求取出前k大个数


# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# heap_sort(li)
# print(li)

#插入元素
# li = [1, 2, 3, 5, 3, 2, 1]
# li.insert(0, 0)
# del li[0]
# num = li.pop(0)
#remove按值进行删除，但只会删除第一个值
# # li.remove(3)
# print(li)


# #列表永久排序sort
# li.sort()
# #倒序输出
# li.sort(reverse=True)
#
# print(li)

# #列表临时排序
# print(sorted(li))

# #倒着打印列表
# li.reverse()
# print(li)

#range包含第一个值到第二个值，但是不包括第二个值,第三个值表示步长

# #复制列表
# lied = li[:]
# print(lied)

#元组元素不可修改，要修改只能重新定义

#字典

#归并排序
# def merge(li, low, mid, high):
#     i = low
#     j = mid + 1
#     ltmp = []
#     while i<=mid and j<=high:
#         if li[i] < li[j]:
#             ltmp.append(li[i])
#             i += 1
#         else:
#             ltmp.append(li[j])
#             j += 1
#     while i <= mid:
#         ltmp.append(li[i])
#         i += 1
#     while j <= high:
#         ltmp.append(li[j])
#         j += 1
#     li[low:high+1] = ltmp
#
# def merge_sort(li, low, high):
#     if low < high:
#         mid = (low + high)//2
#         merge_sort(li, low, mid)
#         merge_sort(li, mid+1, high)
#         merge(li, low, mid, high)

#希尔排序

#计数排序

#桶排序 = 计数排序 + 冒泡排序
#速度取决于列表中元素的分布

#基数排序
#很快，但少用
# def radix_sort(li):
#     max_num = max(li)
#     it = 0
#     while 10 ** it <= max_num:
#         buckets = [[] for _ in range(10)]
#         for var in li:
#             digit = (var // 10 ** it) % 10
#             buckets[digit].append(var)
#         li.clear()
#         for buc in buckets:
#             li.extend(buc)
#         it += 1
#
#
# li = list(range(100))
# import random
# random.shuffle(li)
# print(li)
# radix_sort(li)
# print(li)
#
# w = [64]
# for i in range(1, 100):
#     a = w[i - 1]*0.971+1.25
#     w.append(a)
#     if w[i] <= 55:
#         break
# print(len(w))
# print(w)

#列表和数组有所不同
#列表元素数据类型无需相同  底层原理是列表中储存元素的地址
#数组长度固定  底层原理是python给我们重新开辟一块空间并复制原来的元素过去
# li = []
# a = 1
# b = '2'
# li.append(a)
# li.append(b)
# print(li)
#栈的实现
#一般的列表即可实现栈
#li.append进栈
#li.pop出栈
#li[-1]取栈顶
# def brace_match(s):
#     match = {'}': '{', ']': '[', ')': '('}
#     li = []
#     for ch in s:
#         if ch in {'(', '[', '{'}:
#             li.append(ch)
#         else:
#             if len(li) == 0:
#                 return False
#             elif li[-1] == match[ch]:
#                 li.pop()
#             else:
#                 return False
#     if len(li) == 0:
#         return True
#     else:
#         return False
#
# s = '[][][](){}{{{}}'
# print(brace_match(s))

# from collections import deque
#
# q = deque([1, 2, 3], 3)
# #若在其后加上队列长度，如q=deque([1,2,3],3),则进队操作会挤走一个元素
# q.append(4)#队尾进队
# print(q.popleft())#队首出队
#
# #用于双向队列
# q.appendleft(1)
# q.pop()
# print(q)
# 迷宫问题栈求解，深度优先
# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
#
# dirs = [
#     lambda x, y: (x + 1, y),
#     lambda x, y: (x - 1, y),
#     lambda x, y: (x, y - 1),
#     lambda x, y: (x, y + 1)
# ]
#
#
# def maze_path(x1, y1, x2, y2):
#     stack = []
#     stack.append((x1, y1))
#     while len(stack) > 0:
#         curnode = stack[-1]
#         if curnode[0] == x2 and curnode[1] == y2:
#             for p in stack:
#                 print(p)
#             return True
#         for dir in dirs:
#              nextnode = dir(curnode[0], curnode[1])
#              if maze[nextnode[0]][nextnode[1]] == 0:
#                  stack.append(nextnode)
#                  maze[nextnode[0]][nextnode[1]] = 2
#                  break
#         else:
#             maze[curnode[0]][curnode[1]] = 2
#             stack.pop()
#     else:
#         print("没有路")
#         return False
#
#
# maze_path(1, 1, 8, 8)
#
#
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# def create_linklist_head(li):
#     head = Node(li[0])
#     for element in li[1:]:
#         node = Node(element)
#         node.next = head
#         head = node
#     return head
#
#
# def create_linklist_tail(li):
#     head = Node(li[0])
#     tail = head
#     for element in li[1:]:
#         node = Node(element)
#         tail.next = node
#         tail = node
#     return head
#
#
# def print_linklist(lk):
#     while lk:
#         print(lk.item, end=',')
#         lk = lk.next
#
#
# lk = create_linklist_tail([1, 2, 3, 4])
# print_linklist(lk)





# a = node(1)
# b = node(2)
# c = node(3)
# a.next = b
# b.next = c
# print(a.next.item)


# class LinkList:
#     class Node:
#         def __init__(self, item=None):
#             self.item = item
#             self.next = None

#
# class Animal:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print("%s is eating" % self.name)
#
#
# class Person(Animal):
#
#     def __init__(self, name, age, sex, hobby):
#         # Animal.__init__(self, name, age, sex)
#         super().__init__(name, age, sex)
#         self.hobby = hobby
#
#     def think(self):
#         print("%s is thinking" % self.name)
#
#     def eat(self):
#         # Animal.eat(self)
#         super(Person, self).eat()
#         print("%s is eating quickly" % self.name)
#
# p = Person("11", "23", "m", "打秋")
# p.eat()
# p.think()
# print(p.hobby)
#多继承是深度优先

# s = "abcabc"
# num = 0
# start = 0
# end = 0
# i = 0
# while i < (len(s) - 2):
# # for i, ch in enumerate(s[:len(s) - 2]):
#     a, b, c = 0, 0, 0
#     if s[i] == 'a':
#         a += 1
#     elif s[i] == 'b':
#         b += 1
#     else:
#         c += 1
#     for j, sh in enumerate(s[i + 1:]):
#         if sh == 'a':
#             a += 1
#         elif sh == 'b':
#             b += 1
#         else:
#             c += 1
#         if a > 0 and b > 0 and c > 0:
#             end = i + j + 1
#             x, y, z = 0, 0, 0
#             b = s[i:end]
#             for k, xh in enumerate(b[::-1]):
#                 if xh == 'a':
#                     x += 1
#                 elif xh == 'b':
#                     y += 1
#                 else:
#                     z += 1
#                 if x > 0 and y > 0 and z > 0:
#                     t = len(b) - k
#                     i = j + i + t - 1
#
#                     num += (len(s) - j - 1 - i)
#                     break
#             break
#     i += 1
#
# print(num)

# s = "dsfhoahf"
# s = s[2:6]
# for i, ch in enumerate(s[::-1]):
#     print(i)
#     i += 2
#     print(ch)
#
# strs = ["dsfd", "dsd", "dsfsrf"]
# m = min(strs)
# m = m[:0]
# print(m)

# li1 = [1,2,3]
# li2 = [3,2,1]
# str1 = ''
# for num in li1:
#     str1 = str1 + str(num)
#
# print(int(str1) + 1)
#
# dict = {'1':['1'], '2':['2']}
# dict['1'] = dict.get('1') + ['3']
# print(dict)

# import matplotlib.pyplot as plt
# #一开始的概率
# RLIST = [0.33333]
# DLIST = [0.33333]
# ILIST = [0.33333]
# #计算差分方程组
# for i in range(40):
#     R = RLIST[i]*0.75+DLIST[i]*0.20+ILIST[i]*0.40
#     RLIST.append(R)
#     D = RLIST[i]*0.05+DLIST[i]*0.60+ILIST[i]*0.20
#     DLIST.append(D)
#     I = RLIST[i]*0.20+DLIST[i]*0.20+ILIST[i]*0.40
#     ILIST.append(I)
# #画图
# plt.plot(RLIST)
# plt.plot(DLIST)
# plt.plot(ILIST)
# plt.xlabel('Time')
# plt.ylabel('Voting percent')
# plt.annotate('DemocraticParty',xy = (5,0.2))
# plt.annotate('RepublicanParty',xy = (5,0.5))
# plt.annotate('IndependentCandidate',xy = (5,0.25))
# plt.show()

# dict = {}
# dict['1'] = 1
# print(dict)

# print([i for i in range(1,9)])

# class BiTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#
# a = BiTreeNode('A')
# b = BiTreeNode('B')
# c = BiTreeNode('C')
# d = BiTreeNode('D')
# e = BiTreeNode('E')
# f = BiTreeNode('F')
# g = BiTreeNode('G')
#
# e.lchild = a
# e.rchild = g
# a.rchild = c
# c.lchild = b
# c.rchild = d
# g.rchild = f
#
# root = e
#
# def pre_order(root):
#     if root:
#         print(root.data, end=',')
#         pre_order(root.lchild)
#         pre_order(root.rchild)
#
# def in_order(root):
#     if root:
#         in_order(root.lchild)
#         print(root.data, end=',')
#         in_order(root.rchild)
#
# def post_order(root):
#     if root:
#         post_order(root.lchild)
#         post_order(root.rchild)
#         print(root.data, end=',')
#
# from collections import deque
#
# def level_ordef(root):
#     queue = deque()
#     queue.append(root)
#     while len(queue)>0:
#         node = queue.popleft()
#         print(node.data, end=',')
#         if node.lchild:
#             queue.append(node.lchild)
#         if node.rchild:
#             queue.append(node.rchild)
#
#
# # pre_order(root)
# # in_order(root)
# # post_order(root)
# level_ordef(root)




