import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: π/16
# This is a straightforward division of the constant π by 16
pi_value = mp.pi
result = pi_value / 16

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))