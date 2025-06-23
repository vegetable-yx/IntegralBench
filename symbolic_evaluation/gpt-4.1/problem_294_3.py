import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Maximum m for outer sum: chosen such that (0.25)^m becomes negligible (m=50 ensures 0.25^50 < 1e-30)
max_m = 50
# Maximum n for inner sum: chosen to ensure sufficient convergence for all m, especially m=0
max_n = 40000

# Precompute binomial coefficients for n and denominators for n to optimize inner loop
binom_n_list = []   # Store binomial(0.5, n) for n in [0, max_n]
denom2_list = []    # Store denominators (2n+1) for n in [0, max_n]

for n in range(0, max_n + 1):
    binom_n_list.append(mp.binomial(0.5, n))
    denom2_list.append(mp.mpf(2 * n + 1))

total = mp.mpf(0)   # Initialize total sum

# Outer loop over m from 0 to max_m
for m in range(0, max_m + 1):
    # Compute binomial coefficient for current m
    binom_m = mp.binomial(0.5, m)
    # Compute (-0.25)^m
    sign_power = mp.mpf(-0.25) ** m
    # Compute gamma-dependent part: sqrt(pi) * Gamma(m+0.5) / (2 * Gamma(m+1))
    gamma_numerator = mp.sqrt(mp.pi) * mp.gamma(m + 0.5)
    gamma_denominator = 2 * mp.gamma(m + 1)
    gamma_part = gamma_numerator / gamma_denominator
    # Combine m-dependent factors: binom_m * (-0.25)^m * gamma_part
    term_m = binom_m * sign_power * gamma_part

    inner_sum = mp.mpf(0)   # Initialize inner sum for fixed m
    # Inner loop over n from 0 to max_n
    for n in range(0, max_n + 1):
        # Retrieve precomputed binomial coefficient for n
        binom_n = binom_n_list[n]
        # Retrieve precomputed denominator (2n+1)
        denom2 = denom2_list[n]
        # Compute denominator (m + n + 1)
        denom1 = m + n + 1
        # Compute term: binom_n / (denom1 * denom2)
        term = binom_n / (denom1 * denom2)
        inner_sum += term

    # Multiply inner sum by m-dependent factor and add to total
    total += term_m * inner_sum

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))