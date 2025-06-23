import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the value of pi
pi_value = mp.pi

# Multiply pi by 2 to get the result
result = 2 * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))