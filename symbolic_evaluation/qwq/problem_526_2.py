import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi = mp.pi

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Compute π/4
pi_over_4 = pi / 4

# Multiply components to get final result
result = pi_over_4 * ln_3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))