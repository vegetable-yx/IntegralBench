import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate arcsin(1/3) using mpmath's asin function
arcsin_value = mp.asin(mp.mpf(1)/3)

# Multiply the result by pi
pi_times_arcsin = mp.pi * arcsin_value

# Final result with 10 decimal places
print(mp.nstr(pi_times_arcsin, n=10))