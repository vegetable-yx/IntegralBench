import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Divide π by 4 to get the result
result = pi_value / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))