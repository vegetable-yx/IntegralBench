import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 72 to get the result
result = pi_sq / 72

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))