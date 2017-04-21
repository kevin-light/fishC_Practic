# l = [1,2,3,4]
# a=1
# for i in l:
#     for j in l:
#         for k in l:
#             if (i!=j) and (i!=k) and (j!=k):
#                 a = a+1
#                 print(i,j,k)
# print('循环次数:{}'.format(a))


#NO.002
# I = int(input("当月利润I: "))
# if I <= 100000:
#     print("奖金={}".format(I*10/100))
# elif 100000 <= I <= 200000:
#     print("奖金={}".format(q+(I - 100000)*7.5/100))
# elif 200000 <= I <= 400000:
#     print("奖金={}".format((100000 * 10 / 100)+(200000 - 100000)*7.5/100+(I-200000)*5/100))
# else:
#     print("奖金={}".format((100000 * 10 / 100) + (200000 - 100000) * 7.5 / 100 + (I - 200000) * 5 / 100))

#lainxi实例3
# import math
# for i in range(10000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+268))
#     if (x * x == i + 100) and (y * y == i + 268):
#         print(i)

# for i in range(2,30):
#     print("练习实例：{}".format(i))


# 练习实例：4
# year = int(input("请输入年份：\n"))
# month = int(input("month:\n"))
# day = int(input("day:\n"))
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 <= month <=12:
#     sum = months[month-1] + day
# else:
#     print("data error")
# leap = 0
# if (year%400 == 0) or (year%4 == 0) and (year%100 != 0):
#     leap = 1
# if (leap == 1) and (month>2):
#     sum+=1
# print(sum)



# 练习实例：5
# L = []
# for i in range(3):
#     x = int(input("interger：\n"))
#     L.append(x)
# L.sort()
# print(L)


# 练习实例：6

# def Fib(n):
#     x,y = 1,1
#     for i in range(n - 1):
#         x,y = y,x+y
#     return x
# print(Fib(10))
#
# def fib(n):
#     L = [1,1]
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1,1]
#     for i in range(2,n-1):
#         L.append(L[-2]+L[-1])
#     return L
# print(fib(10))




# # 练习实例：7
# a = [1,2,3]
# b = a[:]
# print(b)
# # 练习实例：8
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i*j))



# 练习实例：9
# import time
# dic = {1:'a',2:'b',3:'c'}
# for key,value in dict.items(dic):
#     print(key,value)
#     #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#     print(time.strftime('%Y-%m-%d %h:%M:%S',time.localtime(time.time())))
#     time.sleep(1)
#     print(time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time())))


# 练习实例：10
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


# 练习实例：11
# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print('%12ld %12ld' % (f1,f2))
#     if (i % 3) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 + f2


# 练习实例：12
# l = []
# for i in range(101,200):
#     for j in range(2,i-1):
#         if i%j ==0:
#             break
#     else:
#         l.append(i)
#
# print(l)
#
# print("总数为：%d" % len(l))

# 练习实例：13
# for n in range(100,1000):
#     i = n // 100
#     j = n //10%10
#     k = n % 10
#     if n == i**3+j**3+k**3:
#         print(n)

# 练习实例：14
# def reduceNum(n):
#     print('{}= '.format(n))
#     if not isinstance(n,int) or n < 0:
#         print('请输入正整数')
#         exit(0)
#     elif n in [1]:
#         print('{}'.format(n))
#     while n not in [1]:
#         for index in range(2,n+1):
#             if n%index == 0:
#                 n /= index
#                 if n == 1:
#                     print(index)
#                 else:
#                     print('{} *'.format(index))
#                 break
# print(reduceNum(90))



# 练习实例：15
# score = int(input('input score: '))
# if score >= 90:
#     grade = 'A'
# elif score >=60:
#     grade = 'B'
# else:
#     grade = 'C'
# print('%d belongs to %s' % (score,grade))


# 练习实例：16
# import time
# ll = time.strftime("%Y-%m-%d %H-%M-%S %A",time.localtime())
# print('本地时间: ',ll)


# import datetime
# if __name__ =='__main__':
#     print(datetime.date.today().strftime('%d/%m/%Y %H/%M/%S'))
#
#     miyaBirthdate = datetime.date(1941,1,5)
#     print(miyaBirthdate.strftime('%d/%m/%Y'))
#
#     miyaBirthdate = miyaBirthdate + datetime.timedelta(days=1)
#     print(miyaBirthdate.strftime('%d/%m/%Y'))
#
#     miyaBirthdate1 = miyaBirthdate.replace(year=miyaBirthdate.year + 1)
#     print(miyaBirthdate1.strftime('%d/%m/%Y'))


# 练习实例：17
# import string
# s = input("input is string : \n")
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print('char=%d,space=%d,digit=%d,other=%d' % (letters,space,digit,others))


# 练习实例：18
# tn = 0
# sn = []
# n = int(input('n= :\n'))
# a = int(input('a = '))
# for count in range(n):
#     tn = tn + a
#     a = a*10
#     sn.append(tn)
#     print(tn)
# sn = lambda x,y : x + y,sn
# print(sum(tn))


# 练习实例：19
# from sys import stdout
# for j in range(2,1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1,j):
#         if j%i == 0:
#             n += 1
#             s -= 1
#             k.append(i)
#     if s == 0:
#         print(j)
#         for i in range(n):
#             stdout.writer(str(k[i]))
#             stdout.writer('')
#         print(k[n])


# 练习实例：20
# hei = 100
# tim = 10
# tour = []
# height = []
# for i in range(1,tim+1):
#     if i == 1:
#         tour.append(hei)
#     else:
#         tour.append(hei*2)
#     hei = hei/2
#     height.append(hei)
# print('zhogngaodu:%s,fantangaodu:%s' % (sum(tour),height[-1]))


# 练习实例：21
# x2 = 1
# for day in range(9,0,-1):
#     x1 = (x2 + 1)*2
#     x2 = x1
# print(x1)

# 练习实例：22
# for a in ['x','y','z']:
#     for b in ['x', 'y', 'z']:
#         for c in ['x', 'y', 'z']:
#             if (a != b)and(b!=c)and(c!=a)and(a!='x')and(c!='x')and(c!='z'):
#                 print('a : %s,b:%s,c:%s' % (a,b,c))

# 练习实例：23
# from sys import stdout
# for i in range(4):
#     for j in range(2 - i + 1):
#         stdout.write(' ')
#     for k in range(2 * i + 1):
#         stdout.write("*")
#     print()
# for i in range(3):
#     for j in range(i + 1):
#         stdout.write(' ')
#     for k in range(4-2*i+1):
#         stdout.write('*')
#     print()
# for i in range(1,5):
#     print(' '*(4-i),end="")
#     for j in range(1,2*i):
#         print('*',end="")
#     print()
# for i in range(3,0,-1):
#     print(' '*(4-i),end='')
#     for j in range(1,2*i):
#         print('*',end='')
#     print()


# 练习实例：24
# a = 2
# b = 1
# s = 0
# for i in range(1,21):
#
#     s1 = a/b
#     a,b = a+b,a
#     s += s1
# print(s)

# 练习实例：25
# s = 0
# a = range(1,21)
# def op(x):
#     r = 1
#     for i in range(1,x+1):
#         r *= i
#     return r
# s = sum(map(op,a))
# print(s)

# s = 0
# def fop(a):
#     r = 1
#     for i in range(1,a+1):
#
#         r *= i
#     return r
# s = sum(map(fop,range(1,21)))
# print(s)

# 练习实例：26

# def fact(a):
#     sum = 0
#     if a == 0:
#         sum = 1
#     else:
#         sum = a * fact(a-1)
#     return sum
# # for i in range(1,6):
# #     print('%d! = %d' % (i,fact(i)))
# print(fact(3))

# 练习实例：27
# a = "1234567"
# print(a[::-1])
# t = list(a)
# t.reverse  #翻转lsit，，list1 = ['Google', 'Runoob', 'Taobao']
# print("".join(t))
#
# s = input('input a string:\n')
# print(s[::-1])

# list(s).reverse
# print("".join(s))

# 练习实例：28
# def order(x):
#     age = 10
#     if x == 1:
#         return age
#
#     else:
#         age += (x-1)*2
#     return age
# print(order(5))



