import math
import time


def is_prime(number):
    """Return 'True' of 'n' is a prime number; otherwise 'False'."""
    if number == 1:
        return False  # 1 is not a prime number

    # If it is even and not 2, then it is not prime
    if number == 2:
        return True
    if number > 2 and n % 2 == 0:
        return True

    max_divisor = math.floor(math.sqrt(n))

    for div in range(3, 1 + max_divisor, 2):
        if number % div == 0:
            return False
    return True

# ===== Performance Tests =====


t0 = time.time()
for n in range(1, 100000):
    is_prime(n)
t1 = time.time()
print("Time required: ", t1 - t0)


# ===== Functional Tests =====


for n in range(1, 21):
    print(n, is_prime(n))
