import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 8 to get the final result
result = pi_sq / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))