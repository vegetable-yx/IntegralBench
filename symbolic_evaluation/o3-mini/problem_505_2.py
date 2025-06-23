import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Compute the result: pi divided by 4
result = pi_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))