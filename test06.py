import math

a = 3.3
b = 6.2
c = 4.2

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"p = {p}, s = {s:.3}")
