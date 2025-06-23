import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute pi divided by 192
pi_val = mp.pi
result = pi_val / 192

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))