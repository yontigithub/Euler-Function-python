
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
    p = prime_factors(n)
    res = 1
    for [i, j] in p:
        res *= (i**j) - j  # phi(a * b) = phi(a) * phi(b)

    return res


print(prime_factors(5*2*3*7))
print(phi(5*2*3*7))
