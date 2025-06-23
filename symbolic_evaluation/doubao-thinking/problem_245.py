import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π squared
pi_squared = mp.pi ** 2

# Multiply by 15
product = 15 * pi_squared

# Divide by 16 to get final result
result = product / 16

# Print result with 10 decimal places
print(mp.nstr(result, n=10))