import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 3
three_sqrt2 = 3 * sqrt_2

# Multiply by pi
product = three_sqrt2 * mp.pi

# Apply negative sign to final result
result = -product

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))