#1、Python生成随机数
# import random
# p1 = random.random()
# print(p1)
# p2 = random.uniform(1,100)
# print(p2)
# p3 = random.randint(1,10)
# print(p3)
# p4 = random.randrange(1,10,2)
# print(p4)
# list=[1,2,3,4,5,6,7]
# p5 = random.choice(list)
# p6 = random.sample(list,2)
# print(p5)
# print(p6)


#2、字符串逆序
# a = "1234567"
# print(a[::-1])
# t = list(a)
# t.reverse
# print("".join(t))

# 3、判断一个字符串是否为回文字符串
# s = "abcdcba"
# s == s[::-1]
# def converted(s):
#     ss = s[:]
#     if len(s) >= 2 and ss[::-1] == s:
#         return True
#     else:
#         return False
# if __name__ == '__main__':
#     s = "12321"
#     print(converted(s))


#4、随机生成100个数，然后写入文件
# import random
# with open("today.txt",'w') as f:
#     for i in range(1, 101):
#         n = random.randint(1,100)
#         f.write(str(n)+"\n")


#6、对列表进行去重
# a = [1,3,2,2,1,5,5,3]
# print(list(set(a)))


#8.有UTF-8编码的文件a.txt。文件路径在E盘根目录，写一段程序逐行读入文本文件。并在屏幕（gbk编码）打印出
# fp = open("C:\pythonfile3.6\fishPractice\today.txt",'r')
# content = fp.read()
# fp.close()
# print(content.decode("utf-8").encode("utf-8","ignore"))