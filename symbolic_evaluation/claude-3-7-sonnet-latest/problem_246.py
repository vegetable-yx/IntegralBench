import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 24
result = 24 * pi_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))