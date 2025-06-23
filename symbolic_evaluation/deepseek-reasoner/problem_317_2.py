import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 4
four_sqrt2 = 4 * sqrt_2

# Multiply by pi
result = four_sqrt2 * mp.pi

# Apply negative sign
result = -result

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))