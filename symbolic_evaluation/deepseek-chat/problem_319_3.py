import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the analytical expression: π/2
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))