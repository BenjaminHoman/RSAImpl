import primes, math

def rsaGenerate(bits):
    e = 65537 #fixed public exponent
    p = None
    q = None
    lamb = None

    while True:
        p = primes.generatePrimeNumber(bits)
        q = primes.generatePrimeNumber(bits)
        if True: #TODO does the public/private pair have a link
            break

if __name__ == "__main__":
    print("RSA implementation")
    #print(
    print(primes.generatePrimeNumber(512))
