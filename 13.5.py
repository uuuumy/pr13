n = int(input())
primes = set(range(2, n))

for p in range(2, int(n**0.5) + 1):
    if p in primes:
        primes.difference_update(range(p * p, n, p))
print(*sorted(primes))