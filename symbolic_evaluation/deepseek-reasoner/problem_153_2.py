import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 16
term = pi_squared / 16

# Subtract 1 from the result
result = term - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))