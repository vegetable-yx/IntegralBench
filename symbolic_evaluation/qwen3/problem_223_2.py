import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = mp.power(pi_value, 3)

# Divide by 4 to get final result
result = pi_cubed / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))