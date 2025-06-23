import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Compute pi divided by 4
result = pi_value / 4

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))