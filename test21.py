high = 100
length = 0

for i in range(10):
    length += high
    print(f"第{i+1}次下落 {high} 米，累计距离 {length} 米")
    high *= 2 / 3
    print(f"第{i+1}次反弹高度 {high} 米")
    if i < 9:
        length += high

print(f"十次落地总距离为 {length} 米")
print(f"第十次反弹高度为 {high} 米")
