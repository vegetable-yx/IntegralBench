import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute arcsin(1/3) using mpmath's asin function
arcsin_value = mp.asin(mp.mpf(1)/3)

# Multiply the result by pi
result = mp.pi * arcsin_value

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))