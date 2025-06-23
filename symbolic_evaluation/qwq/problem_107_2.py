import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 6 to get final result
result = pi_sq / 6

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))