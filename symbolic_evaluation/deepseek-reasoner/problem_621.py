import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the result as -pi/2
result = -pi_value / 2

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))