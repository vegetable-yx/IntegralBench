import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π squared
pi_squared = mp.power(pi_value, 2)

# Calculate numerator (4 * π²)
numerator = mp.mpf(4) * pi_squared

# Divide by 3 to get final result
result = numerator / mp.mpf(3)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))