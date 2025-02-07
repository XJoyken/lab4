import math

n = float(input())
length = float(input())
area = ((n * (length ** 2)) /  4) * (math.cos(math.pi / n) / math.sin(math.pi / n))
print(area)