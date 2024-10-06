def twin_primes(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    return [(p, p + 2) for p in primes if is_prime(p + 2)]
print(twin_primes(20))
