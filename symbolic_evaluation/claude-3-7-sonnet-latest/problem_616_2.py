import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 24
result = pi_sq / 24

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))