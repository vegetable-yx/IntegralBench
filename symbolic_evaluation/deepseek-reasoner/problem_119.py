import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi value using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 16 to get final result
result = pi_cubed / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))