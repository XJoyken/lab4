def even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

print(", ".join(map(str, even(int(input())))))
