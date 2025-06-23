import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Calculate the numerator (3 * pi^3)
numerator = 3 * pi_cubed

# Divide by 32 to get the final result
result = numerator / 32

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))