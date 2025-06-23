import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = mp.power(pi_val, 3)

# Divide by 192 to get final result
result = pi_cubed / 192

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))