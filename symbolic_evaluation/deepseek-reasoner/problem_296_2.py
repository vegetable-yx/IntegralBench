import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the numerator (π² + 4)
numerator = pi_squared + 4

# Divide by 16 to get final result
result = numerator / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))