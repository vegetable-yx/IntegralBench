import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 4 to get final result
result = pi_sq / 4

# Print result with 10 decimal places
print(mp.nstr(result, n=10))