import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed: π^3
pi_cubed = pi_val ** 3

# Divide by 360 to get the final result
result = pi_cubed / 360

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))