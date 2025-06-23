import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the result as pi divided by 8
result = pi_value / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))