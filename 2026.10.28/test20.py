year = int(input("请输入一个年份数字："))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year}是闰年")
if year % 100 == 0 and year % 400 == 0:
    print(f"{year}是闰年")
