import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 2 to get final result
result = pi_sq / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))