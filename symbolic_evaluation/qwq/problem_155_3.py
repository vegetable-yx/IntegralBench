import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 48 to get final result
result = pi_cubed / 48

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))