# 第一题
print("能同时被4和6整除的数是")
for i in range(1, 100, 1):
    if i % 4 == 0 and i % 6 == 0:
        print(i)

print("-" * 60)

s = "西安科技大学历史悠久，底蕴深厚。学校办学历史可以追溯到1895年成立的北洋大学工学院采矿冶金科，1938年迁并于西北工学院矿冶系，1957年并入西安交通大学，1958年从西安交通大学分出成立西安矿业学院，是当时隶属原煤炭工业部仅有的2所5年制本科院校之一。1998年学校实行“中央与地方共建，以地方管理为主”，划转陕西省。1999年更名为西安科技学院，2003年更名为西安科技大学。"

print("序号\t位置")
count = 0
for i in range(0, len(s) - 1, 1):
    if s[i] == "西" and s[i + 1] == "安":
        count += 1
        print(f"{count}\t{i + 1}")

# 第三题
print("-" * 60)
temp = input("请输入一个数字")
final_num = 0

for str in temp[::-1]:
    if str == "-":
        final_num *= -1
    elif str != "0":
        final_num = final_num * 10 + int(str)

print(final_num)
