# 第一题

import math

print("第一题")

sigma_1 = 27.3e6
sigma_3 = 10.7e6
alpha = math.radians(48)  # 角度转弧度

sigma_a = (sigma_1 + sigma_3) / 2 + (sigma_1 - sigma_3) / 2 * math.cos(2 * alpha)
tau_a = (sigma_1 - sigma_3) / 2 * math.sin(2 * alpha)

print(f"法向应力σ_α = {sigma_a:.2f} Pa")
print(f"剪应力τ_α = {tau_a:.2f} Pa")

print("-" * 60)


# 第二题

print("第二题")

pass_cet6 = True  # 是否通过英语六级
avg_score = 83.2  # 总成绩平均分
rank = 9  # 班级总评排名
has_scholarship = True  # 是否获得过国家特等或一等奖学金

qualified = pass_cet6 and avg_score >= 80 and (rank <= 7 or has_scholarship)

if qualified:
    print("该同学具备保研资格")
else:
    print("该同学不具备保研资格")

print("-" * 60)


# 第三题

print("第三题")

"""
分析：
好用的占三个字符, \n占一个字符,  VS占两个字符, " "占一个字符, Cod占三个字符, \x65占一个字符表示e
总计: 3 + 1 + 2 + 1 + 3 + 1 = 11
"""

s = "好用的\nVS Cod\x65"
print(len(s))  # 11
print(s)  # 好用的 换行 VS Code

print("-" * 60)


# 第四题

print("第四题")

my_str = "借问酒家何处有？牧童遥指杏花村。"

str1 = my_str[0:2]  # 切出 '借问'
str2 = my_str[8:10]  # 切出 '牧童'

new_str = str1 + str2
print(new_str)  # 借问牧童

print("-" * 60)


# 第五题

print("第五题")

"""
str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
如果找到了返回索引，如果找不到返回-1
"""

my_str = "'the quick brown fox jumps over a lazy dog'"
is_in_str = my_str.find("jum")
if is_in_str >= 0:
    print(f"{my_str}在改字符串中")
else:
    print(f"{my_str}不在字符串中")

print("-" * 60)


# 第六题

print("第六题")

"""
{value:>+10.4f}
>对齐方式右对齐
+号表示强制打印+/-号
10表示总体占十个字符宽度
.4表示表留4个小数位
f表示易十进制输出

顺序如下：
ormat_spec:             [options][width_and_precision][type]
options:                 [[fill]align][sign]["z"]["#"]["0"]
fill:                    <any character>
align:                   "<" | ">" | "=" | "^"
sign:                    "+" | "-" | " "
width_and_precision:     [width_with_grouping][precision_with_grouping]
width_with_grouping:     [width][grouping]
precision_with_grouping: "." [precision][grouping] | "." grouping
width:                   digit+
precision:               digit+
grouping:                "," | "_"
type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                         | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

temp = math.e
print(f"{temp:>+10.4f}")
