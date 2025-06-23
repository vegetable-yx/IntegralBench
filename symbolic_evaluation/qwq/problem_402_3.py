import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/3
pi_over_3 = mp.pi / 3

# Calculate natural logarithm of π/3
ln_value = mp.log(pi_over_3)

# Multiply by 2 to get final result
result = 2 * ln_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))