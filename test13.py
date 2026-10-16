# 2026年10月10日16:34:59

s1 = "Hello,"
s2 = "world!"
s3 = "Python 程序设计"
c = chr(65)  # 65 是字符 'A' 的码点（Unicode 编码值）

print(len(s1))  # 6
print(len(s3))  # 11（"Python" 6个字符 + "程序设计" 4个字符）
print(s1, s2)  # Hello, world!
print(s1 + s2)  # Hello,world!
print(s3[6])  # 程
print(s3[0:6])  # Python
print(s3[:6])  # Python
print(s3[:-5])  # Python
print(s3[7:])  # 序设计
print("Hello, \nworld!")  # Hello,
# world!
print("Hello, \rman!")  # man!o,
print(len("Hello, \rworld!"))  # 14
print(len(r"Hello, \rworld!"))  # 15
print(len("您\u597d！"))  # 3
print(type(str(33)))  # <class 'str'>
print(c)  # A
print(ord(c))  # 65

print(s1.find("lo"))  # 3
print(s1.startswith("He"))  # True
print(s1.replace("el", "a"))  # Halo,
print(s1.islower())  # False
print(s1.upper())  # HELLO,
