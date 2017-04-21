# for i in range(67,101):
#     print('#练习实例：%d\n\n' % i)

    # 练习实例：67
# def inp(numbers):
#     for i in range(6):
#         numbers.append(int(input("number: ")))
# p = 0
#
# def arr_max(array):
#     max = 0
#     for i in range(1,len(array) - 1):
#         p = i
#         if array[p] >array[max] : max = p
#         k = max()
#         array[0],array[k] = array[k],array[0]
# def arr_min(array):
#     min = 0
#     for i in range(1,len(array) - 1):
#         p = i
#         if array[p] < array[min] : min = p
#     l = min()
#     array[5],array[1] = array[1],array[5]
# def outp(numbers):
#     for i in range(len(numbers)):
#         print(numbers[i])
#
# if __name__ == '__main__':
#     array = []
#     inp(array)
#     arr_max(array)
#     arr_min(array)
#     print('计算：')
#     outp(array)


    # 练习实例：71
# N = 3
# student = []
# for i in range(5):
#     student.append(['','',[]])

    # 练习实例：72
def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n+1,2):
        s += 1.0/i
    return s
def podd(n):
    s = 0.0
    for i in range(1,n+1,2):
        s += 1/i
    return s
def dcall(fp,n):
    s = fp(n)
    return s
if __name__ == '__main__':
    n = int(input('input a number: \n'))
    if n % 2 == 0:
        sum = dcall(peven,n)
    else:
        sum = dcall(podd,n)
    print(sum)


    # 练习实例：73


    # 练习实例：74


    # 练习实例：75


    # 练习实例：76


    # 练习实例：77


    # 练习实例：78


    # 练习实例：79


    # 练习实例：80


    # 练习实例：81


    # 练习实例：82


    # 练习实例：83


    # 练习实例：84


    # 练习实例：85


    # 练习实例：86


    # 练习实例：87


    # 练习实例：88


    # 练习实例：89


    # 练习实例：90


    # 练习实例：91


    # 练习实例：92


    # 练习实例：93


    # 练习实例：94


    # 练习实例：95


    # 练习实例：96


    # 练习实例：97


    # 练习实例：98


    # 练习实例：99


    # 练习实例：100