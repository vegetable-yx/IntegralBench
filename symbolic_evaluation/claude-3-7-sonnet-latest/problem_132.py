import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: π/2
pi_value = mp.pi  # Get the constant π
result = pi_value / 2  # Divide π by 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))