import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 16 to get the result
result = pi_sq / 16

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))