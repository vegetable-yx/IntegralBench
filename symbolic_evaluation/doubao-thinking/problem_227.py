import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Divide by 24 to get the final result
result = pi_squared / 24

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))