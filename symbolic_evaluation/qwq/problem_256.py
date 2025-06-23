import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2 with high precision
sqrt2 = mp.sqrt(2)

# Multiply by 3 and pi
three_pi = 3 * mp.pi
product = three_pi * sqrt2

# Apply negative sign to get final result
result = -product

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))