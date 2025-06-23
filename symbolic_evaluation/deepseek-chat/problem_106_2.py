import mpmath as mp

# Set internal decimal places to 15 for high precision
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = pi_val ** 2

# Divide the squared result by 4
result = pi_squared / 4

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))