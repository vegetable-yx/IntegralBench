import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi cubed
pi_val = mp.pi
pi_cubed = pi_val ** 3

# Denominator value
denominator = 384

# Compute the result: π³ / 384
result = pi_cubed / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))