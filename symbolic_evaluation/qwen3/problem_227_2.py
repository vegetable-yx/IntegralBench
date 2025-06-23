import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 24 to get final result
result = pi_cubed / 24

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))