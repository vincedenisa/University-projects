import random
import math

TWO = 2
THREE = 3
FOUR = 4


def generate_key(bit_length):
    p = blum_prime(bit_length // 2)
    q = blum_prime(bit_length // 2)
    N = p * q
    return N, p, q


def encrypt(m, N):
    return pow(m, TWO, N)


def decrypt(c, p, q):
    N = p * q
    p1 = pow(c, (p + 1) // FOUR, p)
    p2 = p - p1
    q1 = pow(c, (q + 1) // FOUR, q)
    q2 = q - q1

    ext = extended_gcd(p, q)
    y_p = ext[1]
    y_q = ext[2]

    d1 = (y_p * p * q1 + y_q * q * p1) % N
    d2 = (y_p * p * q2 + y_q * q * p1) % N
    d3 = (y_p * p * q1 + y_q * q * p2) % N
    d4 = (y_p * p * q2 + y_q * q * p2) % N

    return d1, d2, d3, d4


def extended_gcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t


def blum_prime(bit_length):
    p = random.getrandbits(bit_length)
    while p % FOUR != THREE or not is_prime(p):
        p = random.getrandbits(bit_length)
    return p


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def random_numbers_implementation():
    key = generate_key(512)
    n, p, q = key
    print("p:", p)
    print("q:", q)
    print("n:", n)
    message = "Hello"
    print("Message sent by sender:", message)

    m = int.from_bytes(message.encode("ascii"), byteorder="big")
    c = encrypt(m, n)
    print("Encrypted Message:", c)

    decrypted_messages = [
        int.from_bytes(decrypt(c, p, q)[i].to_bytes((decrypt(c, p, q)[i].bit_length() + 7) // 8, byteorder='big'),
                       byteorder="big") for i in range(4)]

    final_message = ''.join([dec.to_bytes((dec.bit_length() + 7) // 8, byteorder='big').decode("ascii") for dec in decrypted_messages if dec == m])
    print("Message received by Receiver:", final_message)

if __name__ == "__main__":
    random_numbers_implementation()