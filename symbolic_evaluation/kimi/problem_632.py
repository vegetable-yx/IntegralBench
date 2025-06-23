import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π²/6
pi_sq_over_6 = pi_squared / 6

# Calculate the inner expression (π²/6 - 1)
inner_value = pi_sq_over_6 - 1

# Compute the final natural logarithm
result = mp.log(inner_value)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))