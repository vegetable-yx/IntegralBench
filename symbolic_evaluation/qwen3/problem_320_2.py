import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate 4 divided by pi
pi_value = mp.pi
result = mp.mpf(4) / pi_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))