import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf('0.25'))
gamma_sq = gamma_1_4 ** 2

# Compute the denominator: 16 * sqrt(2 * pi)
denominator = 16 * mp.sqrt(2 * mp.pi)

# Calculate the digamma functions and their difference
digamma_1_4 = mp.digamma(mp.mpf('0.25'))
digamma_3_4 = mp.digamma(mp.mpf('0.75'))
digamma_diff = digamma_1_4 - digamma_3_4

# Combine all parts: (gamma_sq / denominator) * digamma_diff
result = (gamma_sq / denominator) * digamma_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))