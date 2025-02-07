def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for num in squares(int(input())):
    print(num)