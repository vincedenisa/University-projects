# Given natural number n, determine the prime numbers p1
# and p2 such that n = p1 + p2 (check the Goldbach hypothesis).
# Generate all prime numbers less than n.
# test


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 2
    return True

def goldbach_conjecture(n):

    for p1 in range(2, n):
        if is_prime(p1):
            p2 = n - p1
            if is_prime(p2):
                print("The Goldbach conjecture is satisfied for n = {n}: {n} = {p1} + {p2}")
                return
    print("Goldbach's conjecture is not satisfied for n = {n}.")

n = int(input("Enter a natural number: "))
goldbach_conjecture(n)