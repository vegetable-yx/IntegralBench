import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
ln2 = mp.ln(2)

# Square the logarithm value
ln2_squared = ln2 ** 2

# Calculate π/4
pi_over_4 = mp.pi / 4

# Multiply components to get final result
result = pi_over_4 * ln2_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))