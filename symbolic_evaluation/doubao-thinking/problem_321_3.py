import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 4 to get the result
result = pi_sq / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))