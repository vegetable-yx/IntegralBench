import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Get the constant pi
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Calculate the first term: π³/192
term1 = pi_cubed / 192

# Calculate the second term: π/128
term2 = pi_val / 128

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))