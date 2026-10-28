s = input("请输入一串字符")
alpha = 0
space = 0
digit = 0
for i in s:
    if i.isalpha():
        alpha += 1
    if i.isspace():
        space += 1
    if i.isdigit():
        digit += 1

print(
    f"该字符串的字母有{alpha}个， 空格有{space}个， 数字有{digit}个，其他字符有{len(s) - alpha - space - digit}个"
)
