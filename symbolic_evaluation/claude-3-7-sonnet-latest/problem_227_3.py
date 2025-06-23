import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Multiply by 7
seven_pi_cubed = 7 * pi_cubed

# Divide by 48
fraction = seven_pi_cubed / 48

# Apply the negative sign
result = -fraction

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))