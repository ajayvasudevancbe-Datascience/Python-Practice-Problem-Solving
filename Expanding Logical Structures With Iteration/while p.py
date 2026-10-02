def sum_to_n(n):
    counter = 1
    total = 0       
    while(counter <= n):
        total += counter
        counter += 1
    return total

print(sum_to_n(4))