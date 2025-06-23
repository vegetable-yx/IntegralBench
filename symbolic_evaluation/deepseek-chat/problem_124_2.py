import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Compute the analytical expression: pi divided by 4
result = pi_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))