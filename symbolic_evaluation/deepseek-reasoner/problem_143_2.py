import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Compute π/4
pi_over_4 = pi_val / 4

# Multiply components to get final result
result = pi_over_4 * ln2_val

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))