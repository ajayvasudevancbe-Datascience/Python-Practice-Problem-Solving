def nth_prime(n):
   count = 0
   guess = 0
   while count <n:
    guess += 1
    if is_prime(guess):
      count += 1
      return count
nth_prime(0) == 2
nth_prime(1) == 3
nth_prime(3) == 7
        