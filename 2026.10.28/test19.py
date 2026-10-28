num1 = float(input("请输入第 1 个数字："))
num2 = float(input("请输入第 2 个数字："))
num3 = float(input("请输入第 3 个数字："))

# 在此编写判断最大数字的程序片段，并将该数字存储在新变量 largest 中。

largest = 0
if num1 > num2:
    largest = num1

if num3 > largest:
    largest = num3
print("最大数字是", largest)
