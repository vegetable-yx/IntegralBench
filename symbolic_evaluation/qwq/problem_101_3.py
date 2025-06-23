import mpmath as mp
mp.dps = 15

# Calculate square root of 15
sqrt_15 = mp.sqrt(15)

# Compute first term: sqrt(15)/4
term1 = sqrt_15 / 4

# Calculate arcsin(1/4) using mpmath's asin function
arcsin_val = mp.asin(mp.mpf(1)/4)

# Compute second term: (7/2) * arcsin(1/4)
term2 = (mp.mpf(7)/2) * arcsin_val

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))