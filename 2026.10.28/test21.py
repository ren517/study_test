high = 100
length = 0

for i in range(10):
    length += high
    print(f"第{i+1}次落地前下降距离为{high}")
    high *= 2 / 3
    print(f"第{i+1}次反弹高度为{high}")

print(f"十次总距离为{length}")
