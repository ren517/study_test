num = 12

if num < 0:
    print("要输入的数字必须是一个正整数。")
else:
    sum = 0
    temp = num
    # 请补齐此处的代码！
    while temp > 0:
        sum += temp
        temp -= 1
    print(f"直到 {num} 的自然数之和为 {sum}。")
