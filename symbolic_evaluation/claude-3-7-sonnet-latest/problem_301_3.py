import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 8
denominator = 8
divided_term = pi_cubed / denominator

# Apply the negative sign
result = -divided_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))