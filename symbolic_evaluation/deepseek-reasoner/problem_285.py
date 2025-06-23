import mpmath as mp
mp.dps = 15

# Calculate π²/16 term
pi_squared_over_16 = (mp.pi ** 2) / 16

# Calculate ln(1 + √2) term
sqrt2 = mp.sqrt(2)
log_term = mp.log(1 + sqrt2)

# Square the logarithm term and multiply by 0.5
log_squared_half = 0.5 * (log_term ** 2)

# Combine terms for final result
result = pi_squared_over_16 - log_squared_half

print(mp.nstr(result, n=10))