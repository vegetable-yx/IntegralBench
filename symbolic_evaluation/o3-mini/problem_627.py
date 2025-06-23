import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate ln(2)
ln_2 = mp.log(2)

# Calculate (1/2) * ln(2)
half_ln_2 = 0.5 * ln_2

# Combine terms: π/4 - 1 + (1/2)ln(2)
result = pi_over_4 - 1 + half_ln_2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))