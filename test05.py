# name = input('请输入你的名字：')
# city = input('你来自哪个城市？')
# # 请对比以下两行输出结果的差异：
# print('欢迎您！来自', city, '的', name, '。')
# print('欢迎您！来自' + city + '的' + name + '。')

# x = 33  # x 是一个整型变量
# print(x, type(x))  # 33 <class 'int'>

# url = "https://zimo.net/aqjs/"  # url 是一个字符串变量
# print(url, type(url))  # https://zimo.net/aqjs/ <class 'str'>

# is_ready = True
# print(is_ready, type(is_ready))  # True <class 'bool'>

# import math

# a = 33
# b = 0
# c = -22
# d = 2**8
# e = a * c
# f = int("886")
# g = abs(c)
# h = math.ceil(3.3)

# n = 44
# n_2 = 0b101100
# n_8 = 0o54
# n_16 = 0x2C
# # 将打印 True True True
# print(n == n_2, n == n_8, n == n_16)
# # 将打印 44 0b101100 0o54 0x2c
# print(n, bin(n), oct(n), hex(n))

import math

a = 3.0
b = 0.1415
c = -2.78e6
d = 3.14e-2
f = 3 / 2  # 除法运算总是产生一个浮点数
g = 2 * a  # 不同类型的二元运算产生的类型总是会被拓宽
h = float("33")
i = math.sin(2)  # 该函数的返回类型是浮点数

temp = "'好用的\nVS Cod\x65'"
print(len(temp))
