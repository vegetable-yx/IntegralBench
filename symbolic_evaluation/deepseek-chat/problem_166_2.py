import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Divide π by 4 to obtain the result
result = pi_value / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))