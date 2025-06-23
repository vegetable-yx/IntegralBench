import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 6 to get the final result
result = pi_sq / 6

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))