import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the value of pi
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 24 to obtain the final result
result = pi_cubed / 24

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))