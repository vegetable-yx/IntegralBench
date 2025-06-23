import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Get the constant π
pi_val = mp.pi

# Calculate π squared
pi_squared = pi_val ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))