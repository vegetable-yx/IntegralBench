import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate π²/8
pi_squared_over_8 = pi_squared / 8

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Multiply components to get final result
result = pi_squared_over_8 * ln_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))