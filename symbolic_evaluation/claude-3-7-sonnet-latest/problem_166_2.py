import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign mathematical constant π
pi_value = mp.pi

# Compute the analytical expression: π/4
result = pi_value / 4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))