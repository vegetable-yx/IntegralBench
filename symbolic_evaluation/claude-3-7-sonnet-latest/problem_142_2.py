import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Calculate the analytical expression: π/8
result = pi_val / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))