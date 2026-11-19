# 第一题
import random


def coin_toss():
    if random.randrange(2):
        return "正面"
    else:
        return "反面"


print(coin_toss())


# 第四题斐波那契数列


# 非递归法
def fib(n, f):
    for i in range(n):
        if i > 1:
            f.append(f[i - 1] + f[i - 2])
        print(f[i], end=" ")


f = []
f.append(0)
f.append(1)
n = int(input("请输入一个整数n"))

fib(n, f)

print("\n")


# 递归法
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(n):
    print(fib1(i), end=" ")
