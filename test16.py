x = 100
if x == 100:
    print("满分")
else:
    print("上有提升空间")

s = "满分" if x == 100 else "上有提升空间"
print(s)


for i in range(3, 15, 3):
    print(i)

print("-" * 60)

for i in range(3, 15, -3):
    print(i)

print("-" * 60)

for i in range(15, 3, -3):
    print(i)
