import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi divided by 8
result = pi_value / 8

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))