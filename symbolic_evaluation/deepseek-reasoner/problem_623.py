import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate arcsin(1/3) using mpmath's asin function
arcsin_term = mp.asin(mp.mpf(1)/3)

# Multiply the result by pi
result = mp.pi * arcsin_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))