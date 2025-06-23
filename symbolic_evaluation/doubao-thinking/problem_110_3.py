import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the value of pi
pi_val = mp.pi

# Compute pi divided by 2
result = pi_val / 2

# Print the result to 10 significant digits
print(mp.nstr(result, n=10))