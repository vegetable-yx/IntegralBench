import mpmath as mp
mp.dps = 15

# Calculate π/4 using mpmath's pi constant
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Compute 1/2 * ln2 term
half_ln2 = 0.5 * ln_2

# Combine all components: π/4 - 1 + (1/2)ln2
result = pi_over_4 - 1 + half_ln2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))