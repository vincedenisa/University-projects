#9. Algorithm for determining all bases b with respect to which a composite odd number n is strong
 #pseudoprime. Use the repeated squaring modular exponentiation method.


def repeated_squaring_modular_exponentiation(base, exponent, modulus):
    """Computes (base^exponent) mod modulus using repeated squaring."""
    if modulus == 1:
        return 0
    remainder = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            remainder = (remainder * base) % modulus
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus  # Square the base
    return remainder

def get_decomposition(n):
    """Decomposes n-1 into 2^s * t where t is odd."""
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s, n  # s and t

def miller_rabin_test(n, base, s, t):
    """Performs the Miller-Rabin primality test for base 'base'."""
    # Compute base^t % n
    x = repeated_squaring_modular_exponentiation(base, t, n)
    if x == 1 or x == n - 1:
        return True

    # Check the sequence of squarings
    for _ in range(s - 1):
        x = repeated_squaring_modular_exponentiation(x, 2, n)
        if x == n - 1:
            return True

    return False

def test_bases(n):
    """Tests which bases b (from 2 to n-2) make n a strong pseudoprime."""
    bases = []
    s, t = get_decomposition(n - 1)
    for base in range(2, n - 1):
        if miller_rabin_test(n, base, s, t):
            bases.append(base)
    return bases

def main():
    n = int(input("Enter an odd composite number n: "))
    result = test_bases(n)
    if len(result) == 0:
        print("Number is not a strong pseudoprime to any base.")
    else:
        print("Number is a strong pseudoprime to bases:", result)

if __name__ == '__main__':
    main()
