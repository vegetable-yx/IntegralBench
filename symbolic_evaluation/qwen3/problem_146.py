import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression separately
sqrt2 = mp.sqrt(2)    # Compute square root of 2
pi_squared = mp.pi ** 2  # Compute π squared

# Combine components according to the formula (3√2/8)π²
result = (3 * sqrt2 * pi_squared) / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))