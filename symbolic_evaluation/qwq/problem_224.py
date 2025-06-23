import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 8 to get final result
result = pi_sq / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))