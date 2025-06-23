import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 4 to get the final result
result = pi_sq / 4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))