# for i in range(29,61):
#     print('#练习实例：%d\n\n' % i)

#练习实例：29
# x = input('qingshuru: \n')
# l = str(x[::-1])
# j = len(l)
# print("x 的位数 %d: %s" % (j,l))

#练习实例：30
# a = int(input("请输入一个数：\n"))
# x = str(a)
# flag = True
# for i in range(len(x)/2):
#     if x[i] != x[-i-1]:
#         flag = Flase
#         break
# if flag:
#     print("hushu")

#练习实例：31
# letter = input("please input letter: ")
# if letter == 'M':
#     print("Monday")
# elif letter == 'T':
#     letters = input("please letter second: ")
#     if letters == 'u':
#         print('Tuesday')
#     elif letters == 'h':
#         print('Thursday')
#     else:
#         print('input error!')
# else:
#     print('input error0!')

#练习实例：32
# a = ['one','two','three']
# #print(a[::-1])
# a.reverse()
# print(a)


#练习实例：33
# l = [1,2,3]
# s1 = ' , '.join(str(n) for n in l)
# print(s1)
# #练习实例：34
# def hello_world():
#     print('hello')
# def three_hello():
#     for i in range(3):
#         hello_world()
# if __name__ == '__main__':
#     three_hello()


#练习实例：35 文本颜色设置
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print(bcolors.OKBLUE + "警告的颜色字体?" + bcolors.BOLD)

#练习实例：36
# lower = int(input("zhixiaozhi:"))
# upper = int(input("zhuidazhi:"))
# for num in range(lower,upper + 1):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# #练习实例：37
# if __name__ == '__main__':
#     N = 3
#     l = []
#     for i in range(N):
#         l.append(input('请输入一个数字：'))
#     for i in range(N-1):
#         min = i
#         for j in range(i+1,N):
#             if l[min] > l[j]:min = j
#         l[i],l[min] = l[min],l[i]
#     for i in range(N):
#         print(l[i])

#练习实例：39
# if __name__ == '__main__':
#     a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
#     print('original list is:')
#     for i in range(len(a)):
#         print(a[i])
#     number = int(input("insert a new number: \n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] in range(10):
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     for i in range(11):
#         print(a[i])


#练习实例：40
# a = [1,2,3,4,5]
# #a.reverse()
# a = a[::-1]
# print(a)

#练习实例：41
# def varfunc():
#     var = 0
#     print('var = %d' % var)
#     var += 1
# if __name__=='__main__':
#     for i in range(3):
#         varfunc()
#
# class Static:
#     StaticVar = 5
#     def varfunc(self):
#         self.StaticVar += 1
#         print(self.StaticVar)
#
# print(Static.StaticVar)
# a = Static
# for i in range(3):
#     a.varfunc()


#练习实例：42
# num = 2
# def autofunc():
#     num = 1
#     print('insternal block = %d' % num)
#     num += 1
# for i in range(3):
#     print(num)
#     num+= 1
#     autofunc()


#练习实例：43
# class Num:
#     nNum = 1
#     def inc(self):
#         self.nNum += 1
#         print('nNum = %d' % self.nNum)
# if __name__ == '__main__':
#     nNum = 2
#     inst = Num()
#     for i in range(3):
#         nNum += 1
#         print(nNum)
#         inst.inc()

#练习实例：44
# X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
#
# Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
#
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
# for r in result:
#     print(r)


# #练习实例：45
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

#练习实例：46


# while True:
#     x = int(input('number:'))
#     a = x * x
#     if a > 50:
#         print(a)
#     else:
#         break

#练习实例：47
# def exchange(a,b):
#     a,b = b, a
#     return (a,b)
#
# if __name__ == '__main__':
#     x = 10
#     y = 20
#     print('x=%d,y=%d' % (x,y))
#     x,y = exchange(x,y)
#     print('x=%d,y=%d' % (x,y))


#练习实例：48

#练习实例：49
#练习实例：50
# import random
# print(random.uniform(10,20))

#练习实例：51
# if __name__ == '__main__':
#     a = 77
#     b = a & 3
#     print('a & b = %d' % b)
#     b &= 7
#     print('a&b = %d' % b)


#练习实例：56
# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=800, height=600, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0,26):
#         canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()



