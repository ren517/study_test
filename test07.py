# 2026年10月10日16:03:25

i1 = 3
i2 = 12
i3 = 2
f1 = 3.0
f2 = 10.2
s1 = "3"

print(i1 * i2)  # 36
print(i1 - i2)  # -9
print(i1**i3)  # 9
print(float(i1 * i2))  # 36.0
print(i2 / i1)  # 4.0

print("-" * 20)

print(i2 // i1)  # 4
print(i2 % i1)  # 0
print(i1 + i1 * i2 / i3)  # 21.0
print(f1 * f2)  # 30.599999999999998
print(round((f1 * f2), 1))  # 30.6

print(i2 / f1)  # 4.0

print("-" * 20)

print(f2 // f1)  # 3.0
print(f2 % f1)  # 1.1999999999999993
print(round((f2 % f1), 1))  # 1.1999999999999993

print(i3**f1)  # 8.0
print(int(i2 / f1))  # 4
print(str(i2 / f1))  # 4.0

print("-" * 20)

print(i2 / int(s1))  # 4.0
print(i2 / int(f1))  # 4.0
print(abs(i1 - i2))  # 9
print(max(i1, i2))  # 12
print(round(f2 / f1))  # 3
print(round((f2 / f1), 2))  # 3.4
