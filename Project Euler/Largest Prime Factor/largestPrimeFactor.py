try:
    import timing
except ImportError:
    pass

originalNumber = 600851475143

n = originalNumber
m = 2
primeNumbers = []
factors = []

while m <= n:
    if not any(m % p == 0 for p in primeNumbers):
        primeNumbers.append(m)
        if n % m == 0:
            n = n/m
            factors.append(m)
            m = 2
    m += 1


print(f"The largest prime factor in {originalNumber} is {factors[len(factors) - 1]}")
