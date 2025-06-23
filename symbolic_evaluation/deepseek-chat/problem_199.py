import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Divide π by 2 to get the result
result = pi_val / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))