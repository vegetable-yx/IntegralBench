import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π²/2
pi_squared_over_2 = pi_squared / 2

# Calculate (π²/2 - 4)
term = pi_squared_over_2 - 4

# Multiply by √2 to get final result
result = mp.sqrt(2) * term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))