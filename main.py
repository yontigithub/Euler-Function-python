
def prime_factors(n):

    res = []

    for i in range(2, n):
        if n == 1:
            return res

        j = 0
        while n % i == 0:
            j += 1
            n /= i

        if j != 0:
            res.append([i, j])


def phi(n):
    return 4


print(prime_factors(1024))
