import mpmath as mp

# Set the internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Calculate the square root of 2
sqrt2_val = mp.sqrt(2)

# Compute the result: pi divided by square root of 2
result = pi_val / sqrt2_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))