import numpy as np

"""
    Use the Sieve of Eratosthenes to generate a list of
    primes up to the limit.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    returns numpy list of primes
"""
def primesUpUntil(limit):
    bits = np.ones(limit, dtype=bool)
    bits[0], bits[1] = False, False
    for i in range(2, limit):
        if bits[i]:
            bits[i*i::i] = False
    return np.flatnonzero(bits)

if __name__ == "__main__":
    print("RSA implementation")
    print(sieve_of_eratosthenes(100))
