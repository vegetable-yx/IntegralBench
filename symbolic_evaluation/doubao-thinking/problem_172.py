import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Divide by 16 to compute the final result
result = pi_value / 16

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))