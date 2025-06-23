import mpmath as mp

# Set internal precision to 15 decimal places for accurate results
mp.dps = 15

# Compute pi/2
pi_over_2 = mp.pi / 2

# Subtract 1 to get the result
result = pi_over_2 - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))