import mpmath as mp

mp.dps = 15

result = mp.mpf(0)
two = mp.mpf(2)
sqrt_two = mp.sqrt(two)
n = 0

while True:
    # Calculate components of the numerator
    factor = sqrt_two * (two ** (-n))
    gamma1 = mp.gamma((n + 1) / two)
    gamma2 = mp.gamma((n + 2) / two)
    numerator = factor * gamma1 * gamma2

    # Calculate components of the denominator
    denom1 = mp.gamma(n + 1)
    denom1_sq = denom1 ** 2
    denom2 = mp.gamma(n + 3 / two)
    denominator = denom1_sq * denom2

    # Compute the current term and add to result
    term = numerator / denominator
    result += term

    # Check if the term is below the threshold for convergence
    if mp.fabs(term) < 1e-15:
        break

    n += 1

print(mp.nstr(result, n=10))