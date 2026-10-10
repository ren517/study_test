# 2026年10月10日16:39:26

i = 3
print(i > -3)  # True
print(i == 3)  # True
print(i == 3.0)  # True
print(1 < i < 3)  # False
print(1 < i <= 3)  # True

print("-" * 20)  # --------------------

print(i > 1 and i < 3)  # False
print(i > 1 or i < 3)  # True
print(1 < i < 3 and 1 < i <= 3)  # False
print(1 < i < 3 or 1 < i <= 3)  # True
print(not i < 10)  # False

print("-" * 20)  # --------------------

print(False + i)  # 3
print(True + i)  # 4
print(True and i)  # 3
print(False and i)  # False
print(True or i)  # True
