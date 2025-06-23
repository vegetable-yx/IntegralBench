import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 6 to get the result
result = pi_sq / 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))