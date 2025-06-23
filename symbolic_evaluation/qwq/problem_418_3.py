import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute π²/6
term = pi_squared / 6

# Subtract 1 to get the final result
result = term - 1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))