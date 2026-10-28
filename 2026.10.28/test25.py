last = 1
before = 0

for i in range(9):
    before = (last + 1) * 2
    last = before

print(f"最开始有{before}个")
