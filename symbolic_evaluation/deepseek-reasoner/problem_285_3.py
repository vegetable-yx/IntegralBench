import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate numerator (π² - 8)
numerator = pi_squared - 8

# Final result calculation (numerator divided by 16)
result = numerator / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))