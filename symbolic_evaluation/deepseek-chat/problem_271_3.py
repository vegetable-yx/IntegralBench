import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi
pi_val = mp.pi

# Calculate pi squared
pi_squared = pi_val ** 2

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Compute numerator: pi^3 - 4*pi^2 + 3*pi
numerator = pi_cubed - 4 * pi_squared + 3 * pi_val

# Divide numerator by 512 and negate the result
result = -numerator / 512

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))