import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the square of pi
pi_val = mp.pi  # Get the value of pi
result = pi_val ** 2  # Square pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))