def prime_factors(x):
    factors = []
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors.append(d)
            x //= d
        d += 1
    if x > 1:
        factors.append(x)
    return factors

def nth_element_of_sequence(n):
    current_number = 1
    while n > 0:
        factors = prime_factors(current_number)
        for factor in factors:
            if n == 0:
                break
            print(factor, end=", ")
            n -= 1
        current_number += 1

n = int(input("Enter the value of n: "))
print("The {n}-th element of the sequence is:")
nth_element_of_sequence(n)