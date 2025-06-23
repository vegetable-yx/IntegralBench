import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

tolerance = 1e-15
max_k = 1000
total_sum = mp.mpf(0)  # Accumulator for the outer sum
k = 0

while k <= max_k:
    # Precompute denominator factor: 1/(2*(k+2)*4^(k+1))
    base_denom = 2 * (k + 2) * (4**(k + 1))
    base_factor = 1 / mp.mpf(base_denom)

    # Compute gamma ratio: Gamma(k + 5/2) / Gamma(k + 3)
    gamma_num = mp.gamma(k + mp.mpf('2.5'))
    gamma_den = mp.gamma(k + 3)
    gamma_ratio = gamma_num / gamma_den

    # Compute the inner sum over n from 0 to k
    inner_sum = mp.mpf(0)
    for n in range(0, k + 1):
        # Binomial coefficient for (2n choose n)
        binom1 = mp.binomial(2 * n, n)
        # Binomial coefficient for (2(k-n) choose k-n)
        binom2 = mp.binomial(2 * (k - n), k - n)

        # Denominator: (2n+1) * (2(k-n)+1)
        denom = (2 * n + 1) * (2 * (k - n) + 1)

        # Term for this n: binom1 * binom2 / denom
        term_n = binom1 * binom2 / mp.mpf(denom)
        inner_sum += term_n

    # Term for this k: base_factor * gamma_ratio * inner_sum
    term_k = base_factor * gamma_ratio * inner_sum
    total_sum += term_k

    # Break if term_k is below tolerance
    if mp.fabs(term_k) < tolerance:
        break

    k += 1

# Multiply by the constant factor: sqrt(pi)/2
result = (mp.sqrt(mp.pi) / 2) * total_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))