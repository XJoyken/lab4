def reverse(n):
    for i in range(n, 0 - 1, -1):
        yield i

for num in reverse(int(input())):
    print(num)