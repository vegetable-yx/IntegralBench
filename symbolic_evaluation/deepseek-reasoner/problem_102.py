import mpmath as mp
mp.dps = 15  # Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 24 to get final result
result = pi_sq / 24

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))