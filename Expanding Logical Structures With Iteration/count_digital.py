def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1

    return count
print(count_digits(5))
print(count_digits(143))
print(count_digits(136236))
print(count_digits(0))
print(count_digits(-8))
print(count_digits(-8293))