import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate 1/2
half = mp.mpf(1)/2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (1/2) * ln(2)
half_ln2 = half * ln2

# Combine results: π/4 - 1/2 + (1/2) * ln(2)
result = pi_over_4 - half + half_ln2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))