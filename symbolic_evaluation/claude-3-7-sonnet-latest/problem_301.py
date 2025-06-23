import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 8
pi_cubed_over_8 = pi_cubed / 8

# Apply the negative sign
result = -pi_cubed_over_8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))