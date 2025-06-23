import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Cube the π value
pi_cubed = pi_value ** 3

# Divide the cubed π by 72
result = pi_cubed / 72

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))